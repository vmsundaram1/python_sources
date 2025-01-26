# This program performs binary search on a list of values and provides the result based on the match with the given input number. This program is without recursion
# and is a normal implementation of binary search algorithm


def binary_search_func(sorted_array1,val):

 low=0
 high=len(sorted_array1)-1
 value1 = float(val)

 while(high >=low):
  mid = (high+low) // 2  
  if float(sorted_array1[mid]) < value1:
   low=mid+1
  elif float(sorted_array1[mid]) > value1:
   high=mid-1
  else:
   return mid

 return -1


# Input Data Collection 

actual_list = input("Enter the values of the list, separated by commas:\n")

check_value = input("Enter the value to be checked in the list:\n")

print(check_value)

input_list = actual_list.split(",")

length1=len(input_list)	

temp_list=[0]*length1


# Sorting the Input List of Data

for i, val in enumerate(input_list):
    temp_list[i]= float(val)

temp_list.sort()

print(int(length1))
print("The Sorted List is ", temp_list)



# Function Call to determine whether a match is found for a given value in the array/list

final_result = binary_search_func(temp_list,check_value) 

if final_result != -1:
  print("Element is present at the index ", str(final_result)," or at the position", str(final_result+1), "from the start of the array\n")

else:
    print("Element is not present in the given list")