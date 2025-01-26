# This program calculates the difference between two 1 dimensional array lists of Size "n". It used Functions and While Loop.


# Function to calculate the difference between two arrays and returns the difference in a list

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
   diff_Arr.append(round(temp,2)) 
   i=i+1
  print(diff_Arr)
 except:
   print("Data Error: Incorrect Data Value present in one of the elements of the Array!")
   
 return diff_Arr
 
# A Function to collect the Input Arrays/Vectors for Computation of Difference, Incoporates Recursion for Data Validation

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


# Invoke the Input Data Collection Function
  
input_collection_and_processing()
