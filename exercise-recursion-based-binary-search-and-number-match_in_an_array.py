# This program performs binary search on a list of values and provides the result based on the match with the given input number. The algorithm uses recursive function
# calls to peform binary search


def binary_search_func(sorted_array1,low,high,value1):

 val=float(value1)

 if (high >= low):
  mid = (high + low) // 2
  if float(sorted_array1[mid]) == val:
   print(float(sorted_array1[mid]))
   print("I am checked",val, mid)
   return mid
  elif float(sorted_array1[mid]) < val:  
   print("val is greater") 
   print(low,high,mid)
   return binary_search_func(sorted_array1,mid+1,high,val)
  elif float(sorted_array1[mid]) > val:
    print("val is less") 
    print(low,high,mid)
    return binary_search_func(sorted_array1,low,mid-1,val)
 else:
  return -1


# Inout Data Collection 

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

if(length1!=0):
   final_result = binary_search_func(temp_list,0,length1-1,check_value) 
else:
   print("The array/list is empty with no elements. Enter Proper Input Data")


if final_result != -1:
  print("Element is present at the index ", str(final_result)," or at the position", str(final_result+1), "from the start of the array\n")

else:
    print("Element is not present in the given list")