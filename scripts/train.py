#!/usr/bin/env python3
"""CPU-friendly training entry point. Always initializes a new model."""
import argparse, hashlib, json, random
from pathlib import Path
import torch
from tokenizers import Tokenizer
from roninia.config import ModelConfig
from roninia.model import RoninLM

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
    ids=[]
    with a.corpus.open(encoding="utf-8") as stream:
        for line in stream:
            if line.strip(): ids.extend(tok.encode(line.strip()).ids)
    if len(ids)<c.context_length+2: raise SystemExit("Corpus too small for one context window")
    data=torch.tensor(ids,dtype=torch.long)
    if int(data.max())>=c.vocab_size: raise SystemExit("Token ID outside configured vocabulary")
    model=RoninLM(c); opt=torch.optim.AdamW(model.parameters(),lr=a.learning_rate,betas=(0.9,0.95),weight_decay=0.1)
    model.train(); history=[]
    for step in range(1,a.steps+1):
        starts=torch.randint(0,len(data)-c.context_length-1,(a.batch_size,))
        x=torch.stack([data[s:s+c.context_length] for s in starts])
        _,loss=model(x,x); opt.zero_grad(set_to_none=True); loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(),1.0); opt.step()
        if step==1 or step%100==0 or step==a.steps:
            history.append({"step":step,"loss":float(loss.detach())})
            print(json.dumps(history[-1]),flush=True)
    a.output_dir.mkdir(parents=True,exist_ok=True)
    ckpt=a.output_dir/f"checkpoint-{a.steps}.pt"
    torch.save({"model_state_dict":model.state_dict(),"config":c.__dict__,
        "parameter_count":model.parameter_count(),"completed_steps":a.steps,
        "tokenizer_sha256":hashlib.sha256(a.tokenizer.read_bytes()).hexdigest(),
        "history":history},ckpt)
    sha=hashlib.sha256(ckpt.read_bytes()).hexdigest()
    (a.output_dir/"SHA256SUMS").write_text(f"{sha}  {ckpt.name}\n",encoding="utf-8")
    print(json.dumps({"checkpoint":str(ckpt),"sha256":sha,"parameters":model.parameter_count()}))
if __name__=="__main__": main()
