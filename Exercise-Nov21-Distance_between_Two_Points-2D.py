# This program calculates the distance for a 2D co-ordinates represented in Vector Form. It used Functions and While Loop.

import math

# This Function calculates the vector distance by passing two input vectors containing the 2D co-ordinate values

def Calculate_2D_Vector_Distance(Arr1, Arr2):
 i=0
 size=2
 distance=0.0
 sqr_diff_Arr=[]
 temp=0.0
 temp1=0.0
 sum=0.0
 if(len(Arr1)==size and len(Arr2)==size):
  try:
   while (i < size):
    print(Arr1[i])
    print(Arr2[i])
    temp = float(Arr1[i])-float(Arr2[i])
    temp1=temp**2
    sqr_diff_Arr.append(temp1) 
    i=i+1
   print(sqr_diff_Arr)
   for j,val in enumerate(sqr_diff_Arr):
    sum+=val
   print("The sum is ",round(sum,2))
   distance = math.sqrt(sum)
  except:
   print("Data Error: Incorrect Data Value present in one of the elements of the Array!")  
  return distance
 else:
  print("Data Incorrect! Correct number of Entires are requires for 2D vector!")
  return 0;



# A Function to collect the Input Arrays/Vectors for Computation of Distance, Incoporates Recursion for Data Input Validation

def input_collection_and_processing():

 count=2
 
# Check the Collected Arrays/Vectors, format

 done=False
 while(not done):
  Array1=input("Enter the "+str(count)+ " elements of 1st Vector separated by Commas\n")
  Array2=input("Enter the "+str(count)+ " elements of 2nd Vector separated by Commas\n")
  array_one = Array1.split(',')
  array_two = Array2.split(',')
  if(len(array_one)!=len(array_two) or len(array_one)!=count or len(array_two)!=count):
   done=False
   print("Input Data Error: You need the enter correct input data again!")
   input_collection_and_processing()
  done=True
 
 distance_value = Calculate_2D_Vector_Distance(array_one,array_two)
 print("The distance between the 2 two-dimensional vectors is: ", round(distance_value,2))

# Invoke the Input Data Collection Function and Process the Collected 2D vector/array data

input_collection_and_processing()
