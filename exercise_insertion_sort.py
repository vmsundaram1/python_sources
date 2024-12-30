# This program implements the Insertion Sort Algorithm for sorting the integer numbers


# A Function to sort the numbers using the insertion sort algorithm - Sorting is accomplished in 3 steps
 
# 1) Selects the first unsorted element in the 1st loop

# 2) Another internal loop shifts all the elements to the right to find/create the position for unsorted element

# 3) Once position is created in the inner loop, the unsorted element is inserted in the appropriate position


def insertion_sort_execution(arr,array_length):

 array_length=int(array_length)
 j=0

 for i in range(1,array_length):
  print(int(i),arr[i])
  key=int(arr[i])
  j=i-1
  while (j>=0 and int(arr[j]) > key):
   arr[j+1] = int(arr[j])
   j=j-1
  arr[j+1]=key
  arr[j]=int(arr[j])

 print(arr)
 return arr

# Input Data Collection

input_list = []

input_list = input("Enter the integer values of the list, separated by commas:\n")

actual_list = input_list.split(",")

count=len(actual_list)

print(actual_list,count)

# Invoking the Function to execute Bubble Sort algorithm

result=insertion_sort_execution(actual_list,count)

print("The sorted output array using Insertion Sort Algorithm is ", result)
