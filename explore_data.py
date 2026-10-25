from pathlib import Path
from collections import Counter

text = Path('data/input.txt').read_text(encoding='utf-8')

def count_total_char(text):
    return len(text)

def count_unique_char(text):
    return len(set(text))

def get_first_n_char(text, n):
    return text[:n]

def get_unique_char(text):
    return sorted(set(text))

def get_vocab_distribution(text):
    count = Counter(text)
    return count