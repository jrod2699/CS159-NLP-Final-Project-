import nltk
import re
import string
import itertools 
from nltk.translate import AlignedSent, Alignment
from nltk.tokenize import TweetTokenizer


def compile_corpus(english_file, for_file, iterations):
    '''
    Compile a corpus from a multiple files containing English and Foreign
    sentences whose pairs are divided by file. All relevant information 
    MUST BE contained within multiple files -- similar to the files provided
    for assignment 6.
    '''
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
