#This program computes the result of coin toss by considering number of tosses and the 2 possible values are taken with unequal probabilities


import math
#import random
from random import random

# The function that returns the value of "0", "1" with unequal probability, more weightage on "0" and less on "1"

def coin_toss_func(count,p1,p2):

 t1 = float(p1)
 t2 = float(p2) 

# random_num = random.randrange(0,count)
 random_num =  random() 

 print(random_num)

 if(random_num <= t1):
  return 0
 else:
  return 1

# Input Data Collection and Validation

done=False
while(not done):
 number=input("Enter the number of times the coin is tossed: ")
 count=int(number)

 prob1=input("Ënter the probability of returning 0\n")
 prob2=input("Ënter the probability of returning 1\n")

 sum_prob = float(prob1)+float(prob2)
 print("Rounded Value of Total Probability Entered is: ",round(sum_prob,1))

 if(round(sum_prob,1)!=1.0 or round(sum_prob,1) > 1.0):
  print("Incorrect data entered for probability, please ensure that the total of 3 probabilities are equal to 1. Try giving input again\n")
  done=False
 else:
  done=True


#Invoke the Function to determine the correct output result for a toss based on the collected input data 

result=[coin_toss_func(count,prob1,prob2) for i in range(count)]

print(result)


# Evaluate the Sum of result values, number of instances of each result value and Sum/Length of result array obtained for all the tosses


i=0
val=0
sum=0
total0=0
total1=0


for i, val in enumerate(result):
  sum+=val
  if(val==0):
   total0+=1
  elif(val==1):
   total1+=1
  else:
   print("Wrong Value")

print("The number of times 0,1 occurred in",count,"coin tosses are:",total0,",",total1,"respectively")
print("The Sum is ", sum)
print("The Sum/Length ratio of result array is :", sum/len(result))