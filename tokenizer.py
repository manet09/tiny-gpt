from pathlib import Path

text = Path('data/input.txt').read_text(encoding='utf-8')

def build_vocab(text):
    # get all unique char
    unique_char = sorted(set(text))
    #char-to-ID dictionary
    stoi = {ch: i for i, ch in enumerate(unique_char)}
    #ID-to-char dictionary
    itos = {i: ch for i, ch in enumerate(unique_char)}
    return stoi, itos

def encode(text, stoi):
    return [stoi[ch] for ch in text]


def decode(token_ids, itos):
    return ''.join([itos[i] for i in token_ids])

if __name__ == '__main__':
    stoi, itos = build_vocab(text)
    frist_50_char = text[:50]


    print(encode(frist_50_char, stoi))
    print(decode(encode(frist_50_char, stoi), itos))
    
    # assert decode(encode(frist_50_char, stoi), itos) == frist_50_char, "TOKENIZER FAILED!"

    # print("TOKENIZER PASSED!")
