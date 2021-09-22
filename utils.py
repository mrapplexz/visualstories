import string
import math

alphabet = set(string.ascii_letters + "',.?!")


# 8 слов на сэмпл
def preprocess_prompt(prompt, words_for_sample=8):
    last_not_space = True
    line = []
    for char in prompt.strip():
        if char in alphabet:
            line.append(char)
            last_not_space = True
        elif last_not_space:
            last_not_space = False
            line.append(" ")
    words = "".join(line).split()
    samples = [" ".join(words[i * words_for_sample:(i + 1) * words_for_sample]) for i in
               range(math.ceil(len(words) / 8))]
    return samples
