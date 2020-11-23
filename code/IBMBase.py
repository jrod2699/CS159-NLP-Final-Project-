import nltk
import re
import string
from nltk.translate import AlignedSent, Alignment
from nltk.tokenize import TweetTokenizer

def compile_corpus(filename):
    '''
    Compile a corpus from a single data file containing English and Foreign
    sentence pairs that are tab-divided. All relevant information MUST BE
    contained within a single file.
    '''
    corpus = [] 

    f = open(filename, "r")
    
    for line in f:
        # lowercase all words in the line -- this includes eng + for sentence
        line = line.lower()
        strs = line.split("\t")

        # OUR PLAN: split string by tab and index into resultant array to 
        # access the english sentence (first index) and 
        # foreign sentence (2nd index)
        eng_text = strs[0]
        for_text = strs[1]

        # Tokenize on white space
        tokenizer = TweetTokenizer()
        eng_words = tokenizer.tokenize(eng_text)
        for_words = tokenizer.tokenize(for_text)

        # Create alignment pairs and add to corpus
        aligned_sentence = AlignedSent(for_words, eng_words)
        corpus.append(aligned_sentence)
    f.close()

    return corpus

