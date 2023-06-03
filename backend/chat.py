import random
import json
import torch
from backend.train_model import NeuralNet
from backend.nltk_utils import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
