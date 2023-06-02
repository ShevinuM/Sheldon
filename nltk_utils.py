import nltk
import numpy as np
nltk.download('punkt')
from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()

def tokenize(entry):
    return nltk.word_tokenize(entry)

def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_entry, all_words):
    tokenized_entry = [stem(word) for word in tokenized_entry]

    bag = np.zeros(len(all_words), dtype=np.float32)
    for index, word in enumerate(all_words):
        if word in tokenized_entry:
            bag[index] = 1.0

    return bag

