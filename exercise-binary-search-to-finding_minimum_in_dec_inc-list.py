# The binary search is implemented to determine the MINIMUM number in a given array of decreasing numbers first and then followed by increasing numbers.

# A Function to determine the minimum number present in a given array of decreasing and increasing numbers

def determine_minimum(array1):

 print("Inside Function",array1)

 length = len(array1)
 print(length)
 start = 0
 end = length-1


# Checking Empty Array or List or Array with just Space or empty character and returning invaid value

 if(length==0 or (length==1 and array1[0]==' ')):
  return -1

 while start < end:
  mid= int((start+end)//2)
  print(start,end,mid)
  if float(array1[mid]) > float(array1[mid+1]):
   print("I am on the decreasing side",float(array1[mid]),float(array1[mid+1]))
   start = mid+1
  else:
   print("I am on the increasing side",float(array1[mid]),float(array1[mid+1]))
   end = mid-1

 return float(array1[start])


# Input Data Collection for making the Binary Search to determine the maximum number


i_list = input("Enter the List by giving a combination of DECREASING sequence first followed by INCREASING Sequence of numbers ONLY!\n Give each input entry separated by a comma:\n")

input_list = i_list.split(",")

length1=len(input_list)	

print(len(input_list))

print("Before Function Call, the input list is ", input_list)

cnt=determine_minimum(input_list)

print("\n*****************************\n")
print("The MINIMUM in the given sequence of increasing-decreasing numbers is ", cnt)
print("\n*****************************\n")
