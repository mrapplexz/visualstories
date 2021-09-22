import numpy as np
import torch
from transformers import AutoModelWithLMHead
from transformers import AutoTokenizer

from config import available_genres


# todo: add more genres
def get_prefix_for_genre(genre):
    return available_genres[genre]


def generate(args):
    np.random.seed(args.seed)
    torch.manual_seed(args.seed)

    tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neo-2.7B")
    model = AutoModelWithLMHead.from_pretrained("EleutherAI/gpt-neo-2.7B")
    model.to(args.device)
    prefix = get_prefix_for_genre(args.genre)
    data = f"""{prefix} {args.start}"""
    input_data = tokenizer.encode(data, return_tensors="pt")
    out = model.generate(input_ids=input_data.to(args.device),
                         max_length=args.max_length,
                         repetition_penalty=args.repetition_penalty,
                         do_sample=True,
                         top_k=args.top_k,
                         top_p=args.top_p,
                         temperature=args.temperature)
    decoded = tokenizer.decode(out[0])
    return decoded[len(prefix):]
