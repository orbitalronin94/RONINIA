#!/usr/bin/env python3
import argparse, hashlib, json
from pathlib import Path
from tokenizers import Tokenizer, models, pre_tokenizers, decoders, trainers

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--input",required=True,type=Path)
    ap.add_argument("--output",required=True,type=Path)
    ap.add_argument("--vocab-size",type=int,default=16384)
    a=ap.parse_args()
    if a.vocab_size != 16384: raise SystemExit("RONIN-10M fixes vocab_size=16384")
    a.output.mkdir(parents=True,exist_ok=True)
    tok=Tokenizer(models.BPE(unk_token="<|unk|>"))
    tok.pre_tokenizer=pre_tokenizers.ByteLevel(add_prefix_space=False)
    tok.decoder=decoders.ByteLevel()
    trainer=trainers.BpeTrainer(vocab_size=16384,min_frequency=2,
        special_tokens=["<|unk|>","<|bos|>","<|eos|>","<|pad|>"],
        initial_alphabet=pre_tokenizers.ByteLevel.alphabet())
    tok.train([str(a.input)],trainer)
    if tok.get_vocab_size()!=16384: raise RuntimeError(f"Expected 16384 tokens, got {tok.get_vocab_size()}")
    dest=a.output/"tokenizer.json"; tok.save(str(dest))
    manifest={"schema":"roninia-bytelevel-bpe-v1","vocab_size":tok.get_vocab_size(),
        "special_tokens":{s:tok.token_to_id(s) for s in ("<|unk|>","<|bos|>","<|eos|>","<|pad|>")},
        "tokenizer_sha256":hashlib.sha256(dest.read_bytes()).hexdigest()}
    (a.output/"manifest.json").write_text(json.dumps(manifest,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(manifest,indent=2))
if __name__=="__main__": main()
