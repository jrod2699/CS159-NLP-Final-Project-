import nltk
import re
import string
import itertools 
from nltk.translate.ibm1 import IBMModel1, AlignedSent, Alignment
from nltk.tokenize import TweetTokenizer
from nltk.metrics.scores import precision, recall

def preprocess(english_file, for_file, iterations):
    global corpus
    global ibm1 
    corpus = []
    
    with open(english_file) as eng, open (for_file) as foreign:
        for eng_sent, for_sent in zip(eng, foreign):
            # lowercase all words in the line -- this includes eng + for sentence
            eng_sent = eng_sent.lower()
            for_sent = for_sent.lower()

            # Tokenize on white space
            eng_words = eng_sent.split()
            for_words = for_sent.split()

            # Create alignment pairs and add to corpus
            aligned_sentence = AlignedSent(for_words, eng_words)
            corpus.append(aligned_sentence)
        eng.close()
        foreign.close
    # after creating all sentence pairs, we will create and train our IBM 1 Model 
    ibm1 = IBMModel1(corpus, iterations)

def get_alignments(filename):
    f = open(filename, "r")

    for line in f:
        # lowercase all words in the line -- this includes eng + for sentence
        line = line.lower()
        strs = line.split("\t")

        # OUR PLAN: split string by tab, index into english sentence (first index), foreign sentence (2nd index)
        # then, remove any punctuation (using regex).
        # Finally, split by whitespace. We now have resultant eng and foreign array of words
        eng_text = strs[0]
        for_text = strs[1]

        print(eng_text, "\n", for_text)
        print("========================================================")

       # Tokenize on white space
        eng_words = eng_text.split()
        for_words = for_text.split()

        # Upon the initialization of the IBM1 Model, the translation table with the different
        # alignment probablities is created, therefore we will iterate through the different
        # possible alignments and print out the best alignment according to NLTK's estimations

        # test set for calculating Precision and Recall:
        test_set = set()
        for fw in for_words:
            max_prob = 0
            best_word = ""
            for ew in eng_words:
                val = ibm1.translation_table[fw][ew]
                if val > max_prob:
                    max_prob = val
                    best_word = ew
            print(fw, "\t", best_word, "\t", max_prob)
            test_set.add(best_word)
        
        reference_set = set(eng_words)
        print("Precision:", nltk.metrics.precision(reference_set, test_set))
        print("Recall:", nltk.metrics.recall(reference_set, test_set))
    print("========================================================")
    f.close()

def main():
    preprocess("data/10K.en", "data/10K.es", 10)
    get_alignments("data/random.test")


if __name__ == "__main__":
    main()