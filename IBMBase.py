import nltk
import re
import string
from nltk.translate import AlignedSent, Alignment
from nltk.tokenize.stanford import StanfordTokenizer
from nltk.tokenize import TweetTokenizer

def preprocess(filename):
    f = open(filename, "r")
    corpus = []

    for line in f:
        strs = line.split("\t")
        # OUR PLAN: split string by tab, index into english sentence (first index), foreign sentence (2nd index)
            # then, replace add a "space" before any punctuation (using regex).
            # finally, split by whitespace. we now have resultant eng and foreign arrays
        eng_sent = strs[0]
        for_sent = strs[1]

        # Remove punctuation marks from both sentences
        # tokenizer = nltk.RegexpTokenizer(r"\w+")

        tknzr = TweetTokenizer()
        new_eng = tknzr.tokenize(eng_sent)
        new_for = tknzr.tokenize(for_sent)
        
        aligned_sentence = AlignedSent(new_for, new_eng)
        corpus.append(aligned_sentence)
    f.close()

    return corpus

def main():
    print("Testing how a main function works!")

if __name__ == "__main__":
    main()