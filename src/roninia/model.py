import torch
from torch import nn
from torch.nn import functional as F
from .config import ModelConfig

class CausalSelfAttention(nn.Module):
    def __init__(self, c):
        super().__init__()
        self.heads = c.n_heads
        self.head_dim = c.d_model // c.n_heads
        self.qkv = nn.Linear(c.d_model, 3*c.d_model)
        self.proj = nn.Linear(c.d_model, c.d_model)
        self.dropout = c.dropout

    def forward(self, x):
        b, t, d = x.shape
        q, k, v = self.qkv(x).chunk(3, dim=-1)
        shape = (b, t, self.heads, self.head_dim)
        q, k, v = (z.view(shape).transpose(1, 2) for z in (q, k, v))
        y = F.scaled_dot_product_attention(q, k, v, is_causal=True,
            dropout_p=self.dropout if self.training else 0.0)
        return self.proj(y.transpose(1, 2).contiguous().view(b, t, d))

class MLP(nn.Module):
    def __init__(self, c):
        super().__init__()
        self.up = nn.Linear(c.d_model, c.d_ff)
        self.down = nn.Linear(c.d_ff, c.d_model)
    def forward(self, x):
        return self.down(F.gelu(self.up(x)))

class Block(nn.Module):
    def __init__(self, c):
        super().__init__()
        self.norm1 = nn.LayerNorm(c.d_model, eps=c.layer_norm_eps)
        self.attn = CausalSelfAttention(c)
        self.norm2 = nn.LayerNorm(c.d_model, eps=c.layer_norm_eps)
        self.mlp = MLP(c)
    def forward(self, x):
        x = x + self.attn(self.norm1(x))
        return x + self.mlp(self.norm2(x))

class RoninLM(nn.Module):
    """Decoder-only Transformer; all vocabulary rows are trainable."""
    def __init__(self, config=None):
        super().__init__()
        self.config = config or ModelConfig()
        self.config.validate()
        c = self.config
        self.token_embedding = nn.Embedding(c.vocab_size, c.d_model)
        self.position_embedding = nn.Embedding(c.context_length, c.d_model)
        self.blocks = nn.ModuleList(Block(c) for _ in range(c.n_layers))
        self.final_norm = nn.LayerNorm(c.d_model, eps=c.layer_norm_eps)
        self.lm_head = nn.Linear(c.d_model, c.vocab_size, bias=False)
        self.lm_head.weight = self.token_embedding.weight
        self.apply(self._init_weights)

    @staticmethod
    def _init_weights(m):
        if isinstance(m, (nn.Linear, nn.Embedding)):
            nn.init.normal_(m.weight, mean=0.0, std=0.02)
            if isinstance(m, nn.Linear) and m.bias is not None:
                nn.init.zeros_(m.bias)
        elif isinstance(m, nn.LayerNorm):
            nn.init.ones_(m.weight)
            nn.init.zeros_(m.bias)

    def parameter_count(self):
        return sum(p.numel() for p in self.parameters() if p.requires_grad)

    def forward(self, input_ids, labels=None):
        if input_ids.ndim != 2:
            raise ValueError("input_ids must have shape [batch, sequence]")
        if input_ids.size(1) > self.config.context_length:
            raise ValueError("sequence exceeds context length")
        pos = torch.arange(input_ids.size(1), device=input_ids.device).unsqueeze(0)
        x = self.token_embedding(input_ids) + self.position_embedding(pos)
        for block in self.blocks:
            x = block(x)
        logits = self.lm_head(self.final_norm(x))
        loss = None
        if labels is not None:
            if labels.shape != input_ids.shape:
                raise ValueError("labels must match input_ids shape")
            loss = F.cross_entropy(logits[:, :-1].contiguous().view(-1, self.config.vocab_size),
                labels[:, 1:].contiguous().view(-1))
        return logits, loss
