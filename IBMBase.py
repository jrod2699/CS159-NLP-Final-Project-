import nltk
import re
import string

def preprocess(filename):
    f = open(filename, "r")
    for line in f:
        strs = line.split("\t")
        eng_sent = []
        for_sent = strs[1]
         
    f.close()

def main():
    print("Testing how a main function works!")

if __name__ == "__main__":
    main()