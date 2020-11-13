import nltk
import re
import string

def preprocess(filename):
    f = open(filename, "r")
    for line in f:
        strs = line.split("\t")
        # OUR PLAN: split string by tab, index into english sentence (first index), foreign sentence (2nd index)
            # then, replace add a "space" before any punctuation (using regex).
            # finally, split by whitespace. we now have resultant eng and foreign arrays
        eng_sent = []
        for_sent = strs[1]
         
    f.close()

def main():
    print("Testing how a main function works!")

if __name__ == "__main__":
    main()