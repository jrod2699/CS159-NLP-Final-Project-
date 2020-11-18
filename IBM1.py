import nltk
import re
import string
from nltk.translate.ibm1 import IBMModel1, AlignedSent, Alignment
from nltk.tokenize import TweetTokenizer

def preprocess(filename, iterations):
    global corpus
    global ibm1 

    corpus = []
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

    ibm1 = IBMModel1(corpus, iterations)
    # ibm1.__align_all(corpus)
    # print(corpus[2].alignment)
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
                val = ibm1.translation_table[fw][ew]
                if val > max_prob:
                    max_prob = val
                    best_word = ew
            print(fw, "\t", best_word, "\t", max_prob)
            test_set.add(best_word)
        test_sentence = []
        test_sentence.append(AlignedSent(for_words, eng_words))
        print(test_sentence[0].words)
        print(test_sentence[0].mots)
        print(corpus[0].alignment)
        #reference_set = set(eng_words)
        print("Precision:", precision(reference_set, test_set))
        print("Recall:", recall(reference_set, test_set))
       
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
    f.close()

def print_alignments():
    print("Printing")
    # python equivalent of try catch - wrap all of this around that
    for i in range(len(corpus)-1):    
        try:
            print("Foreign Words: ", corpus[i + 1].words)
            print("English Words: ", corpus[i + 1].mots)
            print("Alignments: ", corpus[i + 1].alignment)
        except:
            pass
    print("Done")

def example():
    bitext = []
    bitext.append(AlignedSent(['klein', 'ist', 'das', 'haus'], ['the', 'house', 'is', 'small']))
    bitext.append(AlignedSent(['das', 'haus', 'ist', 'ja', 'groß'], ['the', 'house', 'is', 'big']))
    bitext.append(AlignedSent(['das', 'buch', 'ist', 'ja', 'klein'], ['the', 'book', 'is', 'small']))
    bitext.append(AlignedSent(['das', 'haus'], ['the', 'house']))
    bitext.append(AlignedSent(['das', 'buch'], ['the', 'book']))
    bitext.append(AlignedSent(['ein', 'buch'], ['a', 'book']))
    ibm1 = IBMModel1(bitext, 5)
    print(ibm1.translation_table['buch']['book'])
    print(ibm1.translation_table['das']['book'])
    print(ibm1.translation_table['buch'][None])
    print(ibm1.translation_table['ja'][None])
    test_sentence = bitext[2]
    print(test_sentence.words)
    print(test_sentence.mots)
    print(test_sentence.alignment)


def main():
    preprocess("data/10000french.txt", 5)
    # get_alignments("data/test_sentences.txt")
    print_alignments()
    # example()
    #help(IBMModel1)

if __name__ == "__main__":
    main()