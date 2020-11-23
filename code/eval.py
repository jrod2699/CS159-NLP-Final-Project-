import nltk
import string
import random
from IBMBase import compile_corpus
from nltk.translate import Alignment, alignment_error_rate
from nltk.metrics import precision, recall, f_measure
from nltk.tokenize import TweetTokenizer

def eval(test_alignments):
    f = open(test_alignments, "r")

    for line in f:
        strs = line.split("\t")

        print("-" * 47)
        print(strs[0])
        print(strs[1])

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
        print("AER:", alignment_error_rate(hand_aligns, sys_aligns))
        print("F1: ", f_measure(hand_aligns, sys_aligns))
    
        print("-" * 47, "\n")
    f.close()


def main():
    eval("data/evaluation tests/random.spanish")


if __name__ == "__main__":
    main()