#!/usr/bin/env python3
"""CPU-friendly streaming training entry point. Always initializes a new model."""
import argparse, hashlib, json, random
from pathlib import Path
import numpy as np
import torch
from tokenizers import Tokenizer
from roninia.config import ModelConfig
from roninia.model import RoninLM

def sha256_file(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda:stream.read(8*1024*1024),b""): h.update(chunk)
    return h.hexdigest()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--config",type=Path,required=True)
    ap.add_argument("--corpus",type=Path,required=True)
    ap.add_argument("--tokenizer",type=Path,required=True)
    ap.add_argument("--output-dir",type=Path,default=Path("runs/ronin-10m"))
    ap.add_argument("--steps",type=int,default=1000)
    ap.add_argument("--batch-size",type=int,default=2)
    ap.add_argument("--threads",type=int,default=2)
    ap.add_argument("--learning-rate",type=float,default=3e-4)
    a=ap.parse_args()
    if min(a.steps,a.batch_size,a.threads)<=0: raise SystemExit("steps, batch-size and threads must be positive")
    torch.set_num_threads(a.threads); random.seed(20261110); torch.manual_seed(20261110)
    c=ModelConfig.load(a.config); tok=Tokenizer.from_file(str(a.tokenizer))
    eos=tok.token_to_id("<|eos|>")
    if eos is None: raise SystemExit("Tokenizer manifest is missing <|eos|>")
    a.output_dir.mkdir(parents=True,exist_ok=True)
    token_cache=a.output_dir/"corpus-tokens.u16"
    token_count=0
    # uint16 stores every ID in the fixed 16,384-row vocabulary; stream to disk.
    with token_cache.open("wb") as out, a.corpus.open(encoding="utf-8") as stream:
        for line in stream:
            if line.strip():
                ids=tok.encode(line.strip()).ids
                if ids:
                    np.asarray(ids+[eos],dtype=np.uint16).tofile(out)
                    token_count += len(ids)+1
    if token_count<c.context_length+2: raise SystemExit("Corpus too small for one context window")
    data=np.memmap(token_cache,dtype=np.uint16,mode="r")
    if int(data.max())>=c.vocab_size: raise SystemExit("Token ID outside configured vocabulary")
    model=RoninLM(c); opt=torch.optim.AdamW(model.parameters(),lr=a.learning_rate,betas=(0.9,0.95),weight_decay=0.1)
    model.train(); history=[]
    for step in range(1,a.steps+1):
        starts=torch.randint(0,len(data)-c.context_length-1,(a.batch_size,))
        x=torch.stack([torch.from_numpy(np.asarray(data[int(s):int(s)+c.context_length],dtype=np.int64)) for s in starts])
        _,loss=model(x,x); opt.zero_grad(set_to_none=True); loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(),1.0); opt.step()
        if step==1 or step%100==0 or step==a.steps:
            history.append({"step":step,"loss":float(loss.detach())})
            print(json.dumps(history[-1]),flush=True)
    ckpt=a.output_dir/f"checkpoint-{a.steps}.pt"
    torch.save({"model_state_dict":model.state_dict(),"config":c.__dict__,
        "parameter_count":model.parameter_count(),"completed_steps":a.steps,
        "tokenizer_sha256":sha256_file(a.tokenizer),"corpus_sha256":sha256_file(a.corpus),
        "token_count":token_count,"history":history},ckpt)
    sha=sha256_file(ckpt)
    (a.output_dir/"SHA256SUMS").write_text(f"{sha}  {ckpt.name}\\n",encoding="utf-8")
    token_cache.unlink(missing_ok=True)\n    print(json.dumps({"checkpoint":str(ckpt),"sha256":sha,"parameters":model.parameter_count(),"tokens":token_count}))
if __name__=="__main__": main()
