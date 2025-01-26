# This program computes the result of coin toss by considering number of tosses and the 3 possible values are taken with equal probability

import math
from random import random
#import random

# The function that returns the value of "0", "1" and "2" with equal probability

def coin_toss_func(count):

 number1=int(count)
 a = 0.33
 b = 0.66

# random_num = random.randrange(0,3)

 random_num =  random()
 print(random_num)

# return random_num

 if(random_num <= a):
  return 0
 elif (random_num > a and random_num <= b):
  return 1
 else:
  return 2


# Input Data Collection

number=input("Enter the number of times the coin is tossed: ")
count=int(number)



# Invoke the Function to determine the correct output result for a toss based on the collected input data 

result=[coin_toss_func(count) for i in range(count)]

print(result)

i=0
val=0
sum=0
total0=0
total1=0
total2=0

# Evaluate the Sum of result values, number of instances of each result value and Sum/Length of result array obtained for all the tosses

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