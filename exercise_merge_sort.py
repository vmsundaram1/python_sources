# This program implements the Merge Sort Algorithm (Divide and Conquer) for sorting the integer numbers


# A Function to sort the numbers using the merge sort algorithm - during sorting, it swaps the number to the next adjacent number in the array for every pass 


def merge(array1,l,m,r):
 

 n1 = int(m)-int(l)+1
 n2 = int(r)-int(m)

 print("n1 and n2 are:",n1,n2)

# create temp arrays or lists

 left_array =[0]*n1
 right_array=[0]*n2

 
 for i in range(n1):
  left_array[i]=int(array1[l+i])
  
 for j in range(n2):
  right_array[j]=int(array1[m+1+j])


 print("The left array is",left_array)
 print("The right array is",right_array)

 i=0
 j=0
 k=int(l)

# This loop compares the elementes of both sub-arrays and merges them appropriately

 while(i<n1 and j<n2):
  if(int(left_array[i])<= int(right_array[j])):
   array1[k]=int(left_array[i])
   i+=1
  else:
   array1[k]=int(right_array[j])
   j+=1
  k+=1

# Copies the remaining elements of the left array, if there are any:

 while i < n1:
  array1[k]=int(left_array[i])
  i+=1
  k+=1
  
# Copies the remaining elements of the right array, if there are any:

 while j < n2:
  array1[k]=int(right_array[j])
  j+=1
  k+=1

 print("I am inside merge:\n",array1)
 
 

# Function to process the merge sort algorithm
  

def merge_sort_execution(arr,left,right):
 
 left=int(left)
 right=int(right)

 if(left < right):      
  middle=(left+right)//2  
  print(left,middle,right)
  merge_sort_execution(arr,left,middle)
  merge_sort_execution(arr,middle+1,right)
  merge(arr,left,middle,right) 
 print("The sorted output array using Merge Sort Algorithm is ",arr)


# Input Data Collection

input_list = []

input_list = input("Enter the integer values of the list, separated by commas:\n")

actual_list = input_list.split(",")

count=len(actual_list)

print(actual_list,count)

left=0
right=int(count)-1

# Invoking the Function to execute Bubble Sort algorithm

merge_sort_execution(actual_list,left,right)
