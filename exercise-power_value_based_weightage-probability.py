# This program is used to compute weighted probability values based weighted probabilities expressed as base 10 power values

from random import random

# Function for considering probability list(normal/weighted( for the Coin/Dice and returning Appropriate value for N Faced Coin/Dice

def coin_toss(arr):
 
 k=0
 r=random()
 print(r,arr)

 for k, val in enumerate(arr):
  value=float(val)
  if r < value:
   return k

# Function to convert weightage values to probabilities  


def convert_weightage_to_probability(array_weightage,sum): 

 length_weightage_array = len(array_weightage)
 temp=[0]*length_weightage_array
 print("Inside Function Call")
 print("The sum of weighted probability values is ",sum, array_weightage)
 k=0
 for k in range(length_weightage_array):
  temp[k] = array_weightage[k]/sum 
  print("In the weightage loop:",k,array_weightage, temp)    
 
 
 print("Exiting Function Call") 
 
 return temp
# Input Data Collection and Validation

done=False
while(not done):
 count = input("Enter the number of times the dice is tossed:\n")
 count1 = int(count)

# Collecting the input data i.e Decimal Weightage Values for expressing as Power Probabilities

 weightage_pow_val=[]
 weightage_pow_val=input("Ënter the Decimal weightage values for N Faces separated by commas\n[these decimals are used to raise pow(10) to arrive at the probabilities]:\n")
 weightage_pow_val_modified=weightage_pow_val.split(",")
 length_pow_weightage_array = len(weightage_pow_val_modified)

 temp_val_pow=0
 sum_pow_weightage=0
 
 for c in range(length_pow_weightage_array):
  temp_val_pow = 10**(int(weightage_pow_val_modified[c]))
  print(temp_val_pow)
  sum_pow_weightage+=temp_val_pow
  weightage_pow_val_modified[c] = sum_pow_weightage

 print("The sum of weighted probability values is ",sum_pow_weightage)
 print(weightage_pow_val_modified)

# Invoking Function Call to convert power weightage values to cumlative probability values

 weightage_pow_val_modified =  convert_weightage_to_probability(weightage_pow_val_modified,sum_pow_weightage)

 last_value_pow_weightage_array = float(weightage_pow_val_modified[length_pow_weightage_array-1])

 print("Checking the Last Value of Power Weighted Array: ",last_value_pow_weightage_array)

 if(round(last_value_pow_weightage_array,1)!=1.0 or round(last_value_pow_weightage_array,1) > 1.0):
  print("Incorrect data entered for probability weightage, please ensure that the N number of probabilities are entered and total of N probabilities are equal to 1. Try giving input again\n")
  done=False
 else:
  done=True


print("Before Processing POWER Weighted Probabilities\n")

z=[coin_toss(weightage_pow_val_modified) for i in range(count1)]

print("\nAfter Processing POWER Weighted Probabilities\n")

print("The result is :",z)

print("*********************************************\n")