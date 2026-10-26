from pathlib import Path
import torch

from tokenizer import encode, decode, build_vocab


text = Path('data/input.txt').read_text(encoding='utf-8')

stoi, itos = build_vocab(text)

token_ids = encode(text, stoi)

token_ids_tensor = torch.tensor(token_ids, dtype=torch.long)

split_index = int(0.9 * len(token_ids_tensor))
train_data = token_ids_tensor[:split_index]
val_data = token_ids_tensor[split_index:]

batch_size = 4
block_size = 8

def get_batch(data):
    # generate random starting positions
    ix = torch.randint(len(data) - block_size, (batch_size,))

    x = [data[i:i+block_size] for i in ix]
    y = [data[i+1:i+block_size+1] for i in ix]

    #stack each collection to batch
    x = torch.stack(x)
    y = torch.stack(y)
    
    return x, y

if __name__ == '__main__':
    x, y = get_batch(train_data)
    print(x.shape, y.shape)
    assert x.shape == (batch_size, block_size)
    assert y.shape == (batch_size, block_size)

