import nltk
import random
from preprocess import compile_corpus
from nltk.translate import IBMModel1, AlignedSent, Alignment

def run(filename, iterations):
    # global variables utilized in the assessment of the IBM Model
    global ibm1
    global corpus

    # construct and modify corpus by adding the system alignments to every sentence pair
    corpus = compile_corpus(filename)
    ibm1 = IBMModel1(corpus, iterations)

    # produce random sentences for testing purposes
    get_rand_sent()


def get_rand_sent():
    ''' 
    Redirect the standard output of the program -- i.e. the random sentences --
    and transfer it over to the appropriate file. From there we will take a 
    look at the sentence pair and include the hand alignment (gold standard)
    to proceed with evaluating the IBM model.
    '''
    i = 0
    while i < 20:
        index = random.randint(0, len(corpus))
        try:
            # only print out "valid" sentence pairs
                # valid = sentence pairs with system-created alignments
            print(" ".join(corpus[index].mots), "\t", " ".join(corpus[index].words), "\t", corpus[index].alignment)
            i += 1
        except:
            pass

def main():
    # change the file based on the langauge being tested
    run("data/languages/vie-eng.txt", 5)

if __name__ == "__main__":
    main()
