import nltk
import re
import string
from nltk.translate import AlignedSent, Alignment
from nltk.tokenize import TweetTokenizer

def compile_corpus(filename):
    '''
    Compile a corpus from a single data file containing English and Foreign
    sentence pairs that are tab-divided. All relevant information MUST BE
    contained within a single file.
    '''
    corpus = [] 

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
        aligned_sentence = AlignedSent(for_words, eng_words)
        corpus.append(aligned_sentence)
    f.close()

    return corpus

def get_rand_sent():
    ''' 
    Redirect the standard output of the program -- i.e. the random sentences --
    and transfer it over to the appropriate file. From there we will take a 
    look at the sentence pair and include the hand alignment (gold standard)
    to proceed with evaluating the IBM model.
    '''
    i = 0
    while i < 10:
        index = random.randint(0, len(corpus))
        try:
            # only print out "valid" sentence pairs
                # valid = sentence pairs with system-created alignments
            print(" ".join(corpus[index].words), "\t", " ".join(corpus[index].mots), "\t", corpus[index].alignment)
            i += 1
        except:
            pass
