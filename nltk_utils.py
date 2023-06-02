import nltk

from nltk.stem.porter import PorterStemmer


stemmer = PorterStemmer()

def tokenize(entry):
    return nltk.word_tokenize(entry)

def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_entry, all_words):
    pass


