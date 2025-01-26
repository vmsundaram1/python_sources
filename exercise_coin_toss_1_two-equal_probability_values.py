# This program computes the result of coin toss by considering number of tosses and the 2 possible values are taken with equal probability

import math
from random import random


# The function that returns the one of the values viz. "0" or "1" with equal probability


def coin_toss_func():
 random_num = random()
 if(random_num <= 0.5):
   return 0
 else:
   return 1


# Input Data Collection

number=input("Enter the number of times the coin is tossed: ")
count=int(number)


# Invoke the Function to determine the correct output result for a toss based on the collected input data 


result=[coin_toss_func() for i in range(count)]

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
