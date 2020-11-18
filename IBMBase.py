import nltk
import re
import string
from nltk.translate import AlignedSent, Alignment
from nltk.tokenize import TweetTokenizer

corpus = []

def preprocess(filename):
    global corpus

    f = open(filename, "r")
    

    for line in f:
        # lowercase all words in the line -- this includes eng + for sentence
        line = line.lower()
        strs = line.split("\t")

        # OUR PLAN: split string by tab, index into english sentence (first index), foreign sentence (2nd index)
        # then, replace add a "space" before any punctuation (using regex).
        # finally, split by whitespace. we now have resultant eng and foreign arrays
        eng_text = strs[0]
        for_text = strs[1]

        # Remove punctuation marks from both sentences
        # eng_sent = "".join([char for char in eng_text if char not in string.punctuation])
        # for_sent = "".join([char for char in for_text if char not in string.punctuation])

        # Tokenize on white space
        tokenizer = TweetTokenizer()
        eng_words = tokenizer.tokenize(eng_text)
        for_words = tokenizer.tokenize(for_text)

        # Create alignment pairs and add to corpus
        aligned_sentence = AlignedSent(for_words, eng_words)
        corpus.append(aligned_sentence)
    f.close()

    return corpus

def get_corpus():
    return corpus
