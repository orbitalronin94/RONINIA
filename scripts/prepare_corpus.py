#!/usr/bin/env python3
"""Build deterministic UTF-8 text corpus from admitted JSONL/JSONL.GZ/TXT files."""
import argparse, gzip, hashlib, json
from pathlib import Path
TEXT_KEYS = ("text", "content", "body", "document", "passage", "instruction", "response", "answer")

def extract(v):
    if isinstance(v, str): return v
    if isinstance(v, dict):
        parts = [extract(v[k]) for k in TEXT_KEYS if k in v]
        return "\n".join(x for x in parts if x)
    if isinstance(v, list): return "\n".join(x for item in v if (x := extract(item)))
    return ""

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--input-root", required=True, type=Path)
    ap.add_argument("--output", required=True, type=Path)
    ap.add_argument("--manifest", type=Path, default=Path("data/corpus/corpus-manifest.json"))
    a=ap.parse_args()
    files=sorted(p for p in a.input_root.rglob("*") if p.is_file() and
        (p.suffix in {".txt",".jsonl"} or p.name.endswith(".jsonl.gz")))
    if not files: raise SystemExit(f"No supported files under {a.input_root}")
    a.output.parent.mkdir(parents=True, exist_ok=True)
    total=0; byte_count=0; corpus_hash=hashlib.sha256(); entries=[]
    with a.output.open("w", encoding="utf-8") as out:
        for p in files:
            opener=gzip.open if p.name.endswith(".gz") else open
            count=0; file_hash=hashlib.sha256()
            with opener(p, "rt", encoding="utf-8", errors="replace") as stream:
                for line in stream:
                    line=line.strip()
                    if not line: continue
                    try:
                        value=json.loads(line) if p.suffix == ".jsonl" or p.name.endswith(".jsonl.gz") else line
                        text=extract(value) or (value if isinstance(value,str) else "")
                    except json.JSONDecodeError: text=line
                    text=" ".join(text.split())
                    if len(text)<20: continue
                    payload=(text+"\n").encode("utf-8")
                    out.write(payload.decode("utf-8")); file_hash.update(payload); corpus_hash.update(payload)
                    byte_count+=len(payload); count+=1
            total+=count
            entries.append({"path":str(p.relative_to(a.input_root)),"records":count,"sha256_text":file_hash.hexdigest()})
    if total==0: raise SystemExit("No usable text records")
    manifest={"schema":"roninia-corpus-v1","files":entries,"files_total":len(entries),
        "records_total":total,"text_bytes":byte_count,"corpus_sha256":corpus_hash.hexdigest()}
    a.manifest.parent.mkdir(parents=True,exist_ok=True)
    a.manifest.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({k:manifest[k] for k in ("files_total","records_total","text_bytes","corpus_sha256")},indent=2))
if __name__=="__main__": main()
