# This program calculates the distance for a 3D co-ordinates represented in Vector Form. It used Functions and While Loop.

import math

# This Function calculates the vector distance by passing two input vectors containing the 3D co-ordinate values

def Compute_Sqrt(count,input_arr): 
 i=0
 temp_value=0.0
 temp_value1=0.0
 sqrt_val=0.0
 my_it = iter(input_arr)
 while (i<count):
  temp_value= next(my_it)
  print(temp_value)
  temp_value1+=float(temp_value)
  i+=1
 sqrt_val =  math.sqrt(temp_value1)
 return sqrt_val


def Calculate_3D_Vector_Distance(Arr1, Arr2):
 i=0
 size=3
 distance=0.0
 sqr_diff_Arr=[]
 temp=0.0
 temp1=0.0
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
   distance=Compute_Sqrt(size, sqr_diff_Arr)
  except:
   print("Data Error: Incorrect Data Value present in one of the elements of the Array!")
  return distance  
 else:
  print("Data Incorrect! Correct number of Entires are requires for 2D vector!")
  return 0;




# A Function to collect the Input Arrays/Vectors for Computation of Distance, Incoporates Recursion for Data Input Validation

def input_collection_and_processing():

 count=3
 
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
 
 distance_value = Calculate_3D_Vector_Distance(array_one,array_two)
 print(distance_value)
 print("The distance between the 2 three-dimensional vectors is: ", round(distance_value,2))


# Invoke the Input Data Collection Function and Process the Collected 2D vector/array data

input_collection_and_processing()
