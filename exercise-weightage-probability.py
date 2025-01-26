# This program is used to compute probability values based on weighted probabilities supplied as input data in the form of integer numbers

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


# Collecting the Weightage Values for Probability as Input Data

 weightage_val=[]
 weightage_val=input("Ënter the weightage values for the same number of probabilities (based on the number of faces) separated by commas:\n")
 weightage_val_modified=weightage_val.split(",")
 length_weightage_array = len(weightage_val_modified)

  
 sum_weightage=0
 for c, value1 in enumerate(weightage_val_modified):
  sum_weightage+=float(value1)
  weightage_val_modified[c] = sum_weightage
 
 print("The sum of weighted probability values is ",sum_weightage)
   

# Invoking Function Call to convert weightage values to probability and data validation

 weightage_val_modified =  convert_weightage_to_probability(weightage_val_modified,sum_weightage)

 last_value_weightage_array = float(weightage_val_modified[length_weightage_array-1])

 print("Checking the Last Value of Weighted Array: ",last_value_weightage_array)
 if(round(last_value_weightage_array,1)!=1.0 or round(last_value_weightage_array,1) > 1.0):
  print("Incorrect data entered for probability weightage, please ensure that the N number of probabilities are entered and total of N probabilities are equal to 1. Try giving input again\n")
  done=False
 else:
  done=True
 

print("*********************************************\n")

print("Before Processing Weighted Probabilities\n")

y=[coin_toss(weightage_val_modified) for i in range(count1)]

print("\nAfter Processing Weighted Probabilities\n")

print("The result is :",y)

print("*********************************************\n")