# UNFAIR BIAS PROBLEM - The program that considers that "N different probabilities and returns the value accordingly based on the number of tosses.

import math
#import random
from random import random

# The function that returns the value based on "n" different probabilities 

def coin_toss_func(count,prob1):

 length1 = len(prob1)
 print("The length of probability list is: ",length1)
 print("I am inside the Function Call",prob1)
 array_Temp=[]
 print(count*length1)
 chunk1=0.0

 i=0
 k=0
 my_val = iter(prob1)
 
  
 while (i<length1):
  print("I am inside while loop",i)
  val = next(my_val)
#  chunk1 = float(val)*count
  chunk1 = float(val)
  if i==0:
   array_Temp.append(chunk1)
  else:
   k=i-1
   chunk1 = chunk1+float(array_Temp[k])
   array_Temp.append(chunk1)
  i+=1


 for i, value in enumerate(array_Temp):
  print("The array of cumlative probailities:",value)
    
# random_num = random.randrange(0,count)
# random_num =  count*float(random()) 
 random_num = float(random()) 
 
 print("The generated RANDOM NUMBER is: ",random_num)

 
 length2 = len(array_Temp)
 length2 = int(length2)
 temp_value=0.0
 temp_value1=0.0
 temp_value_prev=0.0
 final_value=0
 j=0
 while j < length2:
  temp_value = float(array_Temp[j])
  if(j==0 and random_num <= temp_value):
   print("I am in the first check")
   final_value=0
   print("The Final Value is ", int(final_value))
   return final_value	
  elif j==length2-1:
   print("I am in the last check")
   final_value=j
   print("The Final Value is ", int(final_value))
   return final_value
  elif j>0:
    temp_value_prev=array_Temp[j-1]
    temp_value1=array_Temp[j+1]
    print("I am in the intermiedate check",j)
    print(random_num, temp_value_prev, temp_value, temp_value1)
    if(random_num <= temp_value and random_num > temp_value_prev):
     final_value=j
     print("The Final Value is ", int(final_value))
     return final_value
    elif(random_num > temp_value and random_num <= temp_value1):
     final_value=j+1
     print("The Final Value is ", int(final_value))
     return final_value
  j+=1


# Input Data Collection and Validation

done=False
while(not done):
 number=input("UnFair Bias Problem:- Enter the number of times the dice-faces are tossed: ")
 count=int(number)  
 Array1 = input("Enter the probabilty values separated by Commas\n")
 array_of_probabilities = Array1.split(',')
 prob_count = len(array_of_probabilities)
 print(prob_count)
 sum_prob=0.0

# Checking the Sum of Probabilities to ensure input data is valid. If invalid data is entered, the code prompts the user to enter input again

 for i,value in enumerate(array_of_probabilities):
  sum_prob+= float(value)

 print("Rounded Value of Total Probability Entered is: ",round(sum_prob,1))
 if(round(sum_prob,1)!=1.0 or round(sum_prob,1) > 1.0):
  print("Incorrect data entered for probability, please ensure that the total of 3 probabilities are equal to 1. Try giving input again\n")
  done=False
 else:
  done=True


#Invoke the Function to determine the correct output result for a toss based on the collected input data 

print("Before Function Call", count, array_of_probabilities)
result=[coin_toss_func(count,array_of_probabilities) for i in range(count)]

print(result)

i=0
val=0
sum=0
total0=0
total1=0
total2=0
total = []

# Evaluate the Sum of result values and Sum/Length of result array obtained for all the tosses

for i, val in enumerate(result):
 sum+=val

print("The Sum is ", sum)
print("The Sum/Length ratio of result array is :", sum/len(result))