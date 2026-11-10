#!/usr/bin/env python3
"""Prepare a clean text stream from the verified MINIRONIN unified corpus."""
import argparse, gzip, hashlib, json, re
from pathlib import Path

EVAL_SPLIT={"test","tests","eval","evaluation","benchmark","benchmarks","validation","valid","dev","holdout"}
EVAL_PATH=re.compile(r"(^|/)(holdout|eval|evaluation|benchmark|benchmarks|test|tests|validation|valid|dev)(/|[-_.])",re.I)

def is_eval(record):
    if EVAL_PATH.search(str(record.get("source_id",""))): return True
    meta=record.get("metadata",{})
    if isinstance(meta,dict):
        return any(isinstance(meta.get(k),str) and meta[k].strip().casefold() in EVAL_SPLIT
                   for k in ("split","partition","subset","usage","purpose","set"))
    return False

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--input-root",required=True,type=Path)
    ap.add_argument("--output",required=True,type=Path)
    ap.add_argument("--manifest",type=Path,default=Path("data/corpus/corpus-manifest.json"))
    a=ap.parse_args()
    sources=sorted(p for p in a.input_root.rglob("*") if p.is_file() and
                   (p.name.endswith((".jsonl.gz",".jsonl",".txt"))))
    if not sources: raise SystemExit(f"No unified corpus files found under {a.input_root}")
    a.output.parent.mkdir(parents=True,exist_ok=True)
    total=0; skipped_synthetic=0; skipped_eval=0; byte_count=0
    corpus_hash=hashlib.sha256(); entries=[]
    with a.output.open("w",encoding="utf-8") as out:
        for p in sources:
            opener=gzip.open if p.name.endswith(".gz") else open
            count=0; synthetic=0; evaluation=0; file_hash=hashlib.sha256()
            with opener(p,"rt",encoding="utf-8",errors="replace") as stream:
                for line in stream:
                    line=line.strip()
                    if not line: continue
                    if p.suffix==".txt":
                        text=line
                    else:
                        try: record=json.loads(line)
                        except json.JSONDecodeError: continue
                        if not isinstance(record,dict): continue
                        if record.get("synthetic") is True:
                            synthetic+=1; skipped_synthetic+=1; continue
                        if is_eval(record):
                            evaluation+=1; skipped_eval+=1; continue
                        text=record.get("text","")
                        if not isinstance(text,str) or not text.strip():
                            # Preserve structured QA rows if an upstream record has no rendered text.
                            q=record.get("question") or record.get("prompt") or record.get("input")
                            ans=record.get("answer") or record.get("target") or record.get("completion")
                            text=f"Pregunta: {q}\\nRespuesta: {ans}" if q is not None and ans is not None else ""
                    text=" ".join(text.split())
                    if len(text)<20: continue
                    payload=(text+"\\n").encode("utf-8")
                    out.write(payload.decode("utf-8")); file_hash.update(payload); corpus_hash.update(payload)
                    byte_count+=len(payload); count+=1
            total+=count
            entries.append({"path":p.name,"records_written":count,"synthetic_excluded":synthetic,
                            "evaluation_excluded":evaluation,"sha256_text":file_hash.hexdigest()})
    if total==0: raise SystemExit("No non-synthetic, non-evaluation source records survived")
    manifest={"schema":"roninia-corpus-v1","source_artifact":"MINIRONIN unified corpus",
        "source_run_id":42523463620,"files":entries,"files_total":len(entries),
        "records_total":total,"synthetic_records_excluded":skipped_synthetic,
        "evaluation_records_excluded":skipped_eval,"text_bytes":byte_count,
        "corpus_sha256":corpus_hash.hexdigest()}
    a.manifest.parent.mkdir(parents=True,exist_ok=True)
    a.manifest.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\\n",encoding="utf-8")
    print(json.dumps({k:manifest[k] for k in ("source_run_id","files_total","records_total",
        "synthetic_records_excluded","evaluation_records_excluded","text_bytes","corpus_sha256")},indent=2))
if __name__=="__main__": main()
