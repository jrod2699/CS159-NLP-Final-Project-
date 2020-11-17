import nltk
import string
from IBMBase import preprocess
from nltk.translate.ibm1 import IBMModel1
from nltk.metrics.scores import precision, recall
from nltk.tokenize import TweetTokenizer

def run(filename, iterations):
    ibm1 = IBMModel1(preprocess(filename), iterations)
    get_alignments(ibm1, "data/test_sentences.txt")

def get_alignments(ibm, filename):
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

        # Remove punctuation marks from both sentences
        # eng_sent = "".join([char for char in eng_text if char not in string.punctuation])
        # for_sent = "".join([char for char in for_text if char not in string.punctuation])

        print(eng_text, "\t", for_text)
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++")

        # Tokenize on white space
        tokenizer = TweetTokenizer()
        eng_words = tokenizer.tokenize(eng_text)
        for_words = tokenizer.tokenize(for_text)

        # Upon the initialization of the IBM1 Model, the translation table with the different
        # alignment probablities is created, therefore we will iterate through the different
        # possible alignments and print out the best alignment according to NLTK's estimations

        # test set for calculating Precision and Recall:
        test_set = set()
        for fw in for_words:
            max_prob = 0
            best_word = ""
            for ew in eng_words:
                val = ibm.translation_table[fw][ew]
                if val > max_prob:
                    max_prob = val
                    best_word = ew
            print(fw, "\t", best_word, "\t", max_prob)
            test_set.add(best_word)

        reference_set = set(eng_words)
        # print("AlignedSent: ", AlignedSent(for_words, test_word))
        print("Precision:", precision(reference_set, test_set))
        print("Recall:", recall(reference_set, test_set))
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
    f.close()


def main():
    run("data/10000french.txt", 5)


if __name__ == "__main__":
    main()
import nltk
import string
from IBMBase import preprocess
from nltk.translate.ibm1 import IBMModel1
from nltk.metrics.scores import precision, recall
from nltk.tokenize import TweetTokenizer

def run(filename, iterations):
    ibm1 = IBMModel1(preprocess(filename), iterations)
    get_alignments(ibm1, "data/test_sentences.txt")

def get_alignments(ibm, filename):
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

        # Remove punctuation marks from both sentences
        # eng_sent = "".join([char for char in eng_text if char not in string.punctuation])
        # for_sent = "".join([char for char in for_text if char not in string.punctuation])

        print(eng_text, "\t", for_text)
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++")

        # Tokenize on white space
        tokenizer = TweetTokenizer()
        eng_words = tokenizer.tokenize(eng_text)
        for_words = tokenizer.tokenize(for_text)

        # Upon the initialization of the IBM1 Model, the translation table with the different
        # alignment probablities is created, therefore we will iterate through the different
        # possible alignments and print out the best alignment according to NLTK's estimations

        # test set for calculating Precision and Recall:
        test_set = set()
        for fw in for_words:
            max_prob = 0
            best_word = ""
            for ew in eng_words:
                val = ibm.translation_table[fw][ew]
                if val > max_prob:
                    max_prob = val
                    best_word = ew
            print(fw, "\t", best_word, "\t", max_prob)
            test_set.add(best_word)

        reference_set = set(eng_words)
        # print("AlignedSent: ", AlignedSent(for_words, test_word))
        print("Precision:", precision(reference_set, test_set))
        print("Recall:", recall(reference_set, test_set))
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
    f.close()


def main():
    run("data/10000french.txt", 5)


if __name__ == "__main__":
    main()
