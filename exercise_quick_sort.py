# This program implements the Merge Sort Algorithm (Divide and Conquer) for sorting the integer numbers


# A Function to sort the numbers using the quick sort algorithm. 

# Select a number as Pivot. Parition the array based on the pivot. 
# After partitioning, all elements smaller than the pivot will be on its left, and all elements greater than the pivot will be on its right. 
# obtain the index of the pivot.Recursively apply the same process to the two partitioned sub-arrays (left and right of the pivot)
# The recursion stops when there is only one element left in the sub-array, as a single element is already sorted

def swap(array1,index1, index2):
  
   array1[index1],array1[index2] = array1[index2],array1[index1]



def partition_array(arr,left,right):
 
 pivot=int(arr[right])

 index=int(left)-1

 for j in range(left,right):
  if(int(arr[j])< pivot):
   index+=1
   swap(arr,index,j)
 
 swap(arr,index + 1,right)

 return index+1 

# Function to process the quick sort algorithm
  

def quick_sort_execution(arr,left,right):
 
 left=int(left)
 right=int(right)

 if(left < right):      

# pi is the partition return index of pivot

  p_index=partition_array(arr,left,right)

  print(left,int(p_index),right)

  quick_sort_execution(arr,left,int(p_index)-1)
  print("The interim-left sorted output array using quick Sort Algorithm is ",arr)
  quick_sort_execution(arr,int(p_index)+1,right)
  print("The interim-right sorted output array using quick Sort Algorithm is ",arr)


# Input Data Collection

input_list = []

input_list = input("Enter the integer values of the list, separated by commas:\n")

actual_list = input_list.split(",")

count=len(actual_list)

print(actual_list,count)

left=0
right=int(count)-1

# Invoking the Function to execute quick Sort algorithm

quick_sort_execution(actual_list,left,right)

print("The FINAL sorted output array using quick sort Algorithm is ",actual_list)