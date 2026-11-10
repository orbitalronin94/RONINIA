import torch
from roninia.config import ModelConfig
from roninia.model import RoninLM

def test_all_vocab_rows_are_active_and_tied():
    m=RoninLM(ModelConfig())
    assert m.token_embedding.weight.shape==(8192,288)
    assert m.lm_head.weight.data_ptr()==m.token_embedding.weight.data_ptr()
    assert m.parameter_count() == 9_831_168

def test_forward_and_loss():
    m=RoninLM(ModelConfig())
    ids=torch.randint(0,8192,(2,16))
    logits,loss=m(ids,ids)
    assert logits.shape==(2,16,8192)
    assert loss is not None and torch.isfinite(loss)
