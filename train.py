import json
from nltk_utils import tokenize, stem, bag_of_words
import numpy as np

import torch 
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from train_model import NeuralNet


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

class ChatDataset(Dataset):
    def __init__(self):
        self.n_samples = len(x_train)
        self.x_data = x_train
        self.y_data = y_train

    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]

    def __len__(self):
        return self.n_samples

num_epochs = 1000
hidden_size = 8
output_size = len(tags)
input_size = len(x_train[0])
learning_rate = 0.001

dataset = ChatDataset()
train_loader = DataLoader(dataset=dataset, batch_size=8, shuffle=True, num_workers=0)

if torch.cuda.is_available():
    device = torch.device('cuda')
else:
    device = torch.device('cpu')

model = NeuralNet(input_size, hidden_size, output_size).to(device)

# Define the loss criterion
criterion = nn.CrossEntropyLoss()

# Define the optimizer
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

# The criterion computes the loss between the predicted outputs and the true labels.
# CrossEntropyLoss is commonly used for multi-class classification tasks.

# The optimizer updates the model's parameters based on computed gradients to minimize the loss.
# Adam optimizer is an adaptive optimization algorithm used for training neural networks.
# It adjusts the learning rate individually for each parameter for faster convergence and better optimization.

for epoch in range(num_epochs):
    # Iterate over the data in the train_loader
    for (words, labels) in train_loader:
        # Move the input data and labels to the specified device
        words = words.to(device)
        labels = labels.to(device)

        # Forward pass: compute predicted outputs
        outputs = model(words)

        # Compute the loss between predicted outputs and true labels
        loss = criterion(outputs, labels)

        # Backward pass: compute gradients and update model parameters
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

# Create a dictionary to store model-related data
data = {
    "model_state": model.state_dict(),  # Save the state dictionary of the trained model
    "input_size": input_size,  # Save the input size used during training
    "output_size": output_size,  # Save the output size used during training
    "hidden_size": hidden_size,  # Save the hidden size used during training
    "all_words": all_words_arr,  # Save the list of all words used during training
    "tags": tags  # Save the list of tags used during training
}

FILE = "data.pth"
torch.save(data, FILE)
