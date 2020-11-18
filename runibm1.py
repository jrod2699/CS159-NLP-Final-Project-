import nltk
import string
import random
from IBMBase import preprocess, get_corpus
from nltk.translate.ibm1 import IBMModel1, AlignedSent, Alignment
from nltk.metrics import precision, recall
from nltk.tokenize import TweetTokenizer

def run(filename, iterations):
    global ibm1
    global corpus
    corpus = preprocess(filename)
    ibm1 = IBMModel1(corpus, iterations)
    # get_rand_sent("data/random.french")
    eval("data/random.french")

def get_rand_sent(newfile):
    #f = open(newfile, "w")
    i = 0
    while i < 10:
        index = random.randint(0, len(corpus))
        try:
            print(" ".join(corpus[index].words), "\t", " ".join(corpus[index].mots), "\t", corpus[index].alignment)
            i += 1
        except:
            pass
    #f.close()


def eval(test_alignments):
    f = open(test_alignments, "r")

    for line in f:
        strs = line.split("\t")
        
        for_words =strs[0].split()
        eng_words = strs[1].split()

        sys_aligns = Alignment.fromstring(strs[2])
        hand_aligns = Alignment.fromstring(strs[3])

        print("Precision: ", precision(hand_aligns, sys_aligns))
        print("Recall: ", recall(hand_aligns, sys_aligns))
    f.close()


def main():
    run("data/languages/10000french.txt", 5)


if __name__ == "__main__":
    main()
