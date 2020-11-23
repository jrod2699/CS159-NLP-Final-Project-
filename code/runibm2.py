import nltk
import string
import random
from IBMBase import compile_corpus
from nltk.translate import IBMModel2, AlignedSent, Alignment
from nltk.metrics import precision, recall
from nltk.tokenize import TweetTokenizer

def run(filename, iterations):
    # global variables utilized in the assessment of the IBM Model
    global ibm2
    global corpus

    # construct and modify corpus by adding the system alignments
    # to every sentence pair    
    corpus = compile_corpus(filename)
    ibm2 = IBMModel2(corpus, iterations)

    # produce the alignments of the test sentences
    get_rand_sent("data/test sentences/ibm2/french.ibm2")

def get_alignments(filename):
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
        # aligned_sentence = AlignedSent(for_words, eng_words)
        
        for a in corpus:
            if(a.mots == eng_words and a.words == for_words):
                print(" ".join(a.words), "\t", " ".join(a.mots), "\t", a.alignment)
    f.close


def main():
    run("data/languages/fra-eng.txt", 5)
    

if __name__ == "__main__":
    main()
