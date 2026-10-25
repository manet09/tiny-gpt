from pathlib import Path
from collections import Counter

text = Path('data/input.txt').read_text(encoding='utf-8'))

def count_total_char(x):
    return len(x)

def count_unique_char(x):
    return len(set(x))

def display_first_300_char(x):
    print(x[:300])

def display_unique_char(x):
    print(sorted(set(x)))

def display_vocab_distribution(x):
    count = Counter(x)
    for char, count in count.items():
        print(f'{char}: {count}')

# print(count_total_char(text))
# print(count_unique_char(text))
# display_first_300_char(text)
# display_unique_char(text)
display_vocab_distribution(text)