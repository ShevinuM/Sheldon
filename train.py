import json
from nltk_utils import tokenize, stem, bag_of_words
import numpy as np
with open('train_data.json', 'r') as f:
    train_datum = json.load(f)

all_words_arr = []
tags = []
combi = []

for train_data in train_datum['intents']:
    tag = train_data['tag']
    tags.append(tag)
    for pattern in train_data['patterns']:
        token = tokenize(pattern)
        all_words_arr.extend(token)
        combi.append((token, tag))

ignore_words = ['?', '!', '.', ',']
all_words_arr = [stem(w) for w in all_words_arr if w not in ignore_words]
all_words_arr = sorted(set(all_words_arr))
tags = sorted(set(tags))

x_train = []
y_train = []
for combination in combi:
    bag = bag_of_words(combination[0], all_words_arr)
    x_train.append(bag)
    label = tags.index(combination[1])
    y_train.append(label)

x_train = np.array(x_train)
y_train = np.array(y_train)




