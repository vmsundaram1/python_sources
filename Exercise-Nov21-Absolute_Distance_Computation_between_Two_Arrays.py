# This program calculates the absolute distance between two 1 dimensional array lists of Size "n" using function, while Loop.


# Function to calculate the abolute difference between two arrays and returns the difference in a list

def Calculate_Vector_Difference(Size1, Arr1, Arr2):
 i=0
 size=0
 size = int(Size1)
 diff_Arr=[]
 try:
  while (i < size):
   print(Arr1[i])
   print(Arr2[i])
   temp = float(Arr1[i])-float(Arr2[i])
   diff_Arr.append(temp) 
   i=i+1
  print(diff_Arr)
 except:
   print("Data Error: Incorrect Data Value present in the Array!")

 return diff_Arr

# Function to calculate the L1 distance - Absolute Distance between two vectors

def Calculate_Absolute_Distance(temp_array1):
 absolute_distance = 0.0
 i=0
 size = len(temp_array1)
 if(size!=0):
  while (i < size):
   print(temp_array1[i])
   absolute_distance+= abs(float(temp_array1[i]))
   i+=1
  print("The calculated L1 absolute distance is :",round(absolute_distance,2))
 return absolute_distance  
 
 
# Function to collect the Input Arrays/Vectors for Computation of Difference, Incoporates Recursion for Data Validation

def input_collection_and_processing():
 Size1=0
 Size1 = input("Enter an integer/decimal value for the size of the Vector: \n")
 count=int(Size1)

# Check the Collected Arrays/Vectors, format

 if(count>=1):
  Array1=input("Enter the "+str(Size1)+ " elements of 1st Vector separated by Commas\n")
  Array2=input("Enter the "+str(Size1)+ " elements of 2nd Vector separated by Commas\n")
  array_one = Array1.split(',')
  array_two = Array2.split(',')
  if(len(array_one)!=len(array_two) or len(array_one)!=count or len(array_two)!=count ):
   print("Input Data Error: You need the enter correct input data again!")
   input_collection_and_processing()
 else:
  print("Do not Enter Values that are Negative or Zero \n")
  Size1 = input("Enter an integer/decimal value for the size of the Vector: \n")

# Pass the two arrays to the Function for Calculating the Array/Vector Difference
 print(Size1)
 Final_Diff = Calculate_Vector_Difference(Size1,array_one,array_two)
 print("The resultant vector containing Difference is: ", Final_Diff)
 Absolute_Distance = Calculate_Absolute_Distance(Final_Diff)
 print("The Absolute Distance is: ", round(Absolute_Distance,2))


# Invoke the Input Data Collection Function
  
input_collection_and_processing()
