# This program computes the result of coin toss by considering number of tosses and the N faces are taken with equal probability

import math
from random import random
#import random

# The function that returns the value of "0" or "1" or... or "N" with equal probability

def coin_toss_func(count,faces):

 number1=int(count)
 faces_1 = int(faces)
 delta = float(1.0/faces_1)

# random_num = random.randrange(0,3)

 random_num =  random()
 print(random_num)

# return random_num

 i=0
 for i in range(faces_1):
   temp_i = float(delta*i)
   temp_i_plus_one =  float(delta*(i+1))
   if(random_num > temp_i and random_num <= temp_i_plus_one):
     print(i, random_num, temp_i, temp_i_plus_one)
     print("\n")
     return i;   

# Input Data Collection


number2=input("Enter the number of faces of the dice/coin: ")
faces = int(number2)

number=input("Enter the number of times the coin is tossed: ")
count=int(number)



# Invoke the Function to determine the correct output result for a toss based on the collected input data 

result=[coin_toss_func(count, faces) for i in range(count)]

print(result)

i=0
val=0
sum=0

# Evaluate the Sum of result values, number of instances of each result value and Sum/Length of result array obtained for all the tosses

for i, val in enumerate(result):
  sum+=val


print("The Sum is ", sum)
print("The Sum/Length ratio of result array is :", sum/len(result))