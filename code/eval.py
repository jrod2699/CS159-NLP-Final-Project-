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
        print(strs[1], "\n")

        ibm1_aligns = Alignment.fromstring(strs[2])
        ibm2_aligns = Alignment.fromstring(strs[3])
        hand_aligns = Alignment.fromstring(strs[4])

        '''
        Evaluate the sentence pair's precisiona and recall by utilizing the
        built in ntlk.metrics precision and recall functions. The functions 
        parameters are the following:
            1. Reference ("Gold Standard"): our hand alignments that follow the same format
            as the system produced alignments
            2. Test: the alignments produced by the model which will be put in
            comparison with the hand alignments 
        '''
        
        print("IBM1 Precision: ", precision(hand_aligns, ibm1_aligns),"\t","IBM2 Precision: ", precision(hand_aligns, ibm2_aligns))
        print("IBM1 Recall: ", recall(hand_aligns, ibm1_aligns),"\t","IBM2 Recall: ", recall(hand_aligns, ibm2_aligns))
        print("IBM1 AER:", alignment_error_rate(hand_aligns, ibm1_aligns), "\t","IBM2 AER: ", alignment_error_rate(hand_aligns, ibm2_aligns))
        print("IBM1 F1: ", f_measure(hand_aligns, ibm1_aligns), "\t","IBM2 F1: ", f_measure(hand_aligns, ibm2_aligns))
        print("-" * 47, "\n")
    f.close()


def main():
    eval("data/evaluation tests/test sentences/test.spanish")


if __name__ == "__main__":
    main()