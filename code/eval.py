import nltk
import string
from nltk.translate import Alignment, alignment_error_rate
from nltk.metrics import precision, recall, f_measure

def eval(test_alignments):
    f = open(test_alignments, "r")

    # initializing our "counters" used for the aggregate scores
    sentence_pairs = 0
    ibm1_precision_sum, ibm1_recall_sum, ibm1_aer_sum, ibm1_f1_sum = 0, 0, 0, 0
    ibm2_precision_sum, ibm2_recall_sum, ibm2_aer_sum, ibm2_f1_sum = 0, 0, 0, 0

    for line in f:
        sentence_pairs += 1

        strs = line.split("\t")

        print("-" * 47)
        print("Length of foreign sentence: ", len(strs[0].split()))
        print(strs[0])
        print(strs[1], "\n")

        ibm1_aligns = Alignment.fromstring(strs[2])
        ibm2_aligns = Alignment.fromstring(strs[3])
        hand_aligns = Alignment.fromstring(strs[4])

        '''
        Evaluate the sentence pair's precisiona and recall by utilizing the
        built in ntlk.metrics precision and recall functions. The functions 
        parameters are the following:
            1. Reference ("Gold Standard"): our hand alignments that follow the same format
            as the system produced alignments
            2. Test: the alignments produced by the model which will be put in
            comparison with the hand alignments 
        '''

        ibm1_precision, ibm1_recall, ibm1_aer, ibm1_f1 = precision(hand_aligns, ibm1_aligns), recall(hand_aligns, ibm1_aligns), \
                                                         alignment_error_rate(hand_aligns, ibm1_aligns), f_measure(hand_aligns, ibm1_aligns)
        
        ibm2_precision, ibm2_recall, ibm2_aer, ibm2_f1 = precision(hand_aligns, ibm2_aligns), recall(hand_aligns, ibm2_aligns), \
                                                         alignment_error_rate(hand_aligns, ibm2_aligns), f_measure(hand_aligns, ibm2_aligns)

        # Add it to our aggregate calculations
        ibm1_precision_sum += ibm1_precision
        ibm1_recall_sum += ibm1_recall
        ibm1_aer_sum += ibm1_aer
        ibm1_f1_sum += ibm1_f1

        ibm2_precision_sum += ibm2_precision
        ibm2_recall_sum += ibm2_recall
        ibm2_aer_sum += ibm2_aer
        ibm2_f1_sum += ibm2_f1

        
        print("IBM1 Precision: ", ibm1_precision,"\t","IBM2 Precision: ", ibm2_precision)
        print("IBM1 Recall: ", ibm1_recall,"\t","IBM2 Recall: ", ibm2_recall)
        print("IBM1 AER:", ibm1_aer, "\t","IBM2 AER: ", ibm2_aer)
        print("IBM1 F1: ", ibm1_f1, "\t","IBM2 F1: ", ibm2_f1)
        print("-" * 47, "\n")
    f.close()

    # Prints out the total statistics of the dataset
    print("-"*23, "AVERAGE STATS","-"*23)
    print("Average IBM1 Precision: ", ibm1_precision_sum / sentence_pairs,"\t"*2,"Average IBM2 Precision: ", ibm2_precision_sum / sentence_pairs)
    print("Average IBM1 Recall: ", ibm1_recall_sum / sentence_pairs,"\t"*2,"Average IBM2 Recall: ", ibm2_recall_sum / sentence_pairs)
    print("Average IBM1 AER:", ibm1_aer_sum / sentence_pairs, "\t"*2,"Average IBM2 AER: ", ibm2_aer_sum / sentence_pairs)
    print("Average IBM1 F1: ", ibm1_f1_sum / sentence_pairs, "\t"*2,"Average IBM2 F1: ", ibm2_f1_sum / sentence_pairs)
    


def main():
    # change the file based on the langauge being tested
    eval("data/evaluation tests/test sentences/test.viet")

if __name__ == "__main__":
    main()