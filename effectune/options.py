from dataclasses import dataclass, field
from typing import Optional

@dataclass
class GenerationArguments:
    """
    Arguments pertaining to which model/config/tokenizer we are going to fine-tune from.
    """
    min_length: Optional[int] = field(
        default=10,
        metadata={
            "help": "minimal generation length"
        },
    )

    max_length: Optional[int] = field(
        default=128,
        metadata={
            "help": "max generation length"
        },
    )

    num_beams: Optional[int] = field(
        default=5,
        metadata={
            "help": "minimal generation length"
        },
    )

    no_repeat_ngram_size: Optional[int] = field(
        default=0,
        metadata={
            "help": "minimal generation length"
        },
    )

@dataclass
class TuneArguments:
    use_prefix: Optional[str] = field(
        default="none",
        metadata={
            "help": "",
            "choices": ["lisa", "lisa_nomlp", "learn_bias", "luna", "none", "dlisa", "adapter"]
        },
    )

    mid_dim: Optional[int] = field(
        default=800,
        metadata={
            "help": ""
        },
    )

    preseqlen: Optional[int] = field(
        default=200,
        metadata={
            "help": ""
        },
    )

    prefix_dropout: Optional[float] = field(
        default=0.0,
        metadata={
            "help": ""
        },
    )

    unfreeze_params: Optional[str] = field(
        default="none",
        metadata={
            "help": ""
        },
    )

    luna_option: Optional[str] = field(
        default="full_layer",
        metadata={
            "help": "", "choices": ["self_attn", "full_layer", "full_before", "full_after"]
        },
    )

    num_bias_layers: Optional[int] = field(
        default=1,
        metadata={
            "help": ""
        },
    )

    share_luna_params: Optional[int] = field(
        default=1,
        metadata={
            "help": ""
        },
    )

    lisa_option: Optional[str] = field(
        default="default",
        metadata={
            "help": "", \
            "choices": ["default", "cross_attn", "cross_attn_gate",
                "cross_attn_noln", "cross_attn_plug", "mh_adaptor",
                "with_adapter", "cross_attn_before_norm",
                "cross_attn_cz", "attn_adapter", "cross_attn_plug_before_outproj"]
        },
    )


    mh_reuse_proj: Optional[bool] = field(
        default=False,
        metadata={
            "help": ""
        },
    )

    init_with_bert: Optional[int] = field(
        default=1,
        metadata={
            "help": ""
        },
    )

    # down_size: Optional[int] = field(
    #     default=0,
    #     metadata={
    #         "help": ""
    #     },
    # )

# @dataclass
# class TuneArguments:
#     """
#     Arguments pertaining to which model/config/tokenizer we are going to fine-tune from.
#     """





