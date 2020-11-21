import nltk
import string
import random
from IBMBase import compile_corpus
from nltk.translate import IBMModel1, AlignedSent, Alignment
from nltk.metrics import precision, recall
from nltk.tokenize import TweetTokenizer

def run(filename, iterations):
    # global variables utilized in the assessment of the IBM Model
    global ibm1
    global corpus

    # construct and modify corpus by adding the system alignments
    # to every sentence pair
    corpus = compile_corpus(filename)
    ibm1 = IBMModel1(corpus, iterations)

    # produce random sentences for testing purposes
    get_rand_sent("data/rand_out.test")


def eval(test_alignments):
    f = open(test_alignments, "r")

    for line in f:
        strs = line.split("\t")

        sys_aligns = Alignment.fromstring(strs[2])
        hand_aligns = Alignment.fromstring(strs[3])

        '''
        Evaluate the sentence pair's precisiona and recall by utilizing the
        built in ntlk.metrics precision and recall functions. The functions 
        parameters are the following:
            1. Reference ("Gold Standard"): our hand alignments that follow the same format
            as the system produced alignments
            2. Test: the alignments produced by the model which will be put in
            comparison with the hand alignments 
        '''
        print("Precision: ", precision(hand_aligns, sys_aligns))
        print("Recall: ", recall(hand_aligns, sys_aligns))
    f.close()


def main():
    # run("data/languages/10000french.txt", 5)


if __name__ == "__main__":
    main()
