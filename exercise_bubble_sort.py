# This program implements the Bubble Sort Algorithm for sorting the integer numbers


# A Function to sort the numbers using the bubble sort algorithm - during sorting, it swaps the number to the next adjacent number in the array for every pass 

def bubble_sort_execution(arr,array_length):

 j=0
 jmax=0
 array_length=int(array_length)

 for i in range(array_length):
  arr[i]=int(arr[i])
  jmax = array_length-int(i)-1
  j=0
  while j < jmax:
   if(int(arr[j]) > int(arr[j+1])):
    arr[j],arr[j+1] = int(arr[j+1]),int(arr[j])
   j+=1

 print(arr)
 return arr

# Input Data Collection

input_list = []

input_list = input("Enter the integer values of the list, separated by commas:\n")

actual_list = input_list.split(",")

count=len(actual_list)

print(actual_list,count)

# Invoking the Function to execute Bubble Sort algorithm

result=bubble_sort_execution(actual_list,count)

print("The sorted output array using Bubble Sort Algorithm is ", result)
