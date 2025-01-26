# BLEU (bilingual evaluation understudy) is an algorithm for evaluating the quality of text which has been machine-translated from one natural language to another. 
# The BLEU score compares a sentence against one or more reference sentences and tells how well does the candidate sentence matched the list of reference sentence.
# The typical value of BLEU Score ranges between 0 and 1.

import math


candidate_text_number = input("Enter the number of words in the candidate text: ")
reference_text_number = input("Enter the number of words in the reference text: ")

candidate_n = int(candidate_text_number)
reference_n = int(reference_text_number)


temp=0.0
brevity_penalty=0.0

if(candidate_text_number <= reference_text_number):
	temp = 1.0 - (reference_n/candidate_n)
	brevity_penalty = 1.0 - (math.e**temp)
else:
	brevity_penalty =  candidate_n/reference_n


print(brevity_penalty) 

n_gram_size = input("Enter the number of n-gram sizes utilized as an integer number: ")

precision_rating = input("Enter the Precision Rating for the n-gram size: ")

n_grams = int(n_gram_size)
weight_n =  1.0/n_grams

precision_r =  float(precision_rating) 


print("Brevity Penalty: ", brevity_penalty)
print("Weight N: ", weight_n) 
print("Precision Rating: ", precision_r)

temp_1 = math.log(precision_r)
temp_2 = weight_n + temp_1
temp_3 =  (math.e)**temp_2

BLEU_Score = brevity_penalty*temp_3


print("The BLEU SCore is :", BLEU_Score)