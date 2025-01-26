# UNFAIR BIAS PROBLEM - The program that considers that 3 different probabilities and returns the value accordingly based on the number of tosses.

import math
#import random
from random import random

# The function that returns the value of "0", "1" and "2" with different probabilities with more weightage on "0", less weightage on "1" and least weightage on "2"


def coin_toss_func(count,p1,p2,p3):

 t1 = float(p1)
 t2 = float(p2) 
 t3 = float(p3)

# random_num = random.randrange(0,count)
 random_num =  random() 

 print(random_num)

 temp = t1+t2

 if(random_num <= t1):
  return 0
 elif(random_num > t1 and random_num <= temp):
  return 1
 else:
  return 2


# Input Data Collection and Validation

done=False
while(not done):
 number=input("UnFair Bias Problem:- Enter the number of times the coin is tossed: ")
 count=int(number)
 prob1=input("Ënter the probability of returning 0\n")
 prob2=input("Ënter the probability of returning 1\n")
 prob3=input("Ënter the probability of returning 2\n")

# Checking the Sum of Probabilities to ensure input data is valid. If invalid data is entered, the code prompts the user to enter input again

 sum_prob = float(prob1)+float(prob2)+float(prob3)
 print("Rounded Value of Total Probability Entered is: ",round(sum_prob,1))

 if(round(sum_prob,1)!=1.0 or round(sum_prob,1) > 1.0):
  print("Incorrect data entered for probability, please ensure that the total of 3 probabilities are equal to 1. Try giving input again\n")
  done=False
 else:
  done=True

#Invoke the Function to determine the correct output result for a toss based on the collected input data 
 
result=[coin_toss_func(count,prob1,prob2,prob3) for i in range(count)]

print(result)

i=0
val=0
sum=0
total0=0
total1=0
total2=0

# Evaluate the Sum of result values, Sum/Length ratio obtained for all the tosses and also the count for each of the result values

for i, val in enumerate(result):
  sum+=val
  if(val==0):
   total0+=1
  elif(val==1):
   total1+=1
  elif(val==2):
   total2+=1
  else:
   print("Wrong Value")

print("The number of times 0,1,2 occurred in",count,"coin tosses are:",total0,",",total1,",",total2,"respectively")
print("The Sum is ", sum)
print("The Sum/Length ratio of result array is :", sum/len(result))