import nltk
from IBMBase import preprocess
from nltk.translate import AlignedSent, Alignment
from nltk.translate.ibm1 import IBMModel1
from nltk.tokenize.stanford import StanfordTokenizer
from nltk.tokenize import TweetTokenizer

def run(filename, iterations):
    ibm1 = IBMModel1(preprocess(filename), iterations)
    get_alignments(ibm1, "data/test_sentences.txt")

def get_alignments(ibm, filename):
    f = open(filename, "r")

    for line in f:
        strs = line.split("\t")
        # OUR PLAN: split string by tab, index into english sentence (first index), foreign sentence (2nd index)
            # then, replace add a "space" before any punctuation (using regex).
            # finally, split by whitespace. we now have resultant eng and foreign arrays
        eng_sent = strs[0]
        for_sent = strs[1]

        print(eng_sent, "\t", for_sent)

        # Remove punctuation marks from both sentences
        # tokenizer = nltk.RegexpTokenizer(r"\w+")
        tknzr = TweetTokenizer()
        new_eng = tknzr.tokenize(eng_sent)
        new_for = tknzr.tokenize(for_sent)
        
        # align_sent = AlignedSent(new_for, new_eng)

        for fw in new_for:
            ewtable = ibm.translation_table[fw]
            max = 0
            maxWord = ""
            for ew in new_eng:
                # print(new_eng)
                # print('ew: ', ew)
                val = ibm.translation_table[fw][ew]
                if val > max:
                    max = val
                    maxWord = ew
            print(fw, "\t", ew, "\t", max)

    f.close()

def main():
    run("data/10000french.txt", 5)

if __name__ == "__main__":
    main()