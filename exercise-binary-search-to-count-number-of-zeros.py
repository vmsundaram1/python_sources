# In a sorted list of 0s and 1s, the count of 0s (zeros) are determined. The sorting is done separately even if the input of zeros and ones are provided in unsorted 
# manner. The binary search is implemented to determine the number of zeros by narrowing down.

# A Function to determine the number of 0s (zeroes) present in a given array or list containing binary numbers viz. 0s(zeros) and 1s(ones).

def determine_count_of_zeros(array1):

 print("Inside Function",array1)
 count_of_zeros=0
 length = len(array1)
 print(length)
 start = 0
 end = length-1
 count=0

# Checking Empty Array or List or Array with just Space or empty character and returning invaid value

 if(length==0 or (length==1 and array1[0]==' ')):
  return -1

 while start<=end:

  mid=(start+end)//2 

  print(start,end,mid)

  if(int(array1[mid])==0):

   start=mid+1

   count_of_zeros=mid+1

  elif (int(array1[mid])==1):

   end=mid-1
      
 return count_of_zeros


# Input Data Collection for making the Binary Search for counting 0s(Zeroes)


i_list = input("Enter the List by giving a combination of '0s(zeroes) or 1s(Ones)' ONLY!\nGive each input entry separated by a comma:\n")

input_list = i_list.split(",")

length1=len(input_list)	

#input_list = [0,0,0,0,0,1,1,1,1,1,0]

print(len(input_list))

input_list.sort()

print("Before Function Call, the sorted input list is ", input_list)

cnt=determine_count_of_zeros(input_list)

print("\n*****************************\n")
print("The count of zeros is ", cnt)
print("\n*****************************\n")

# Compares the given test case where the expected value is the count of zeroes and the function computing the zero count is tested via these test cases. 

# EXPECTED COUNT of zeroes is given for each test case

test_cases = [
 ([0],1),
 ([0,1,1], 1),
 ([0,0,1], 2),
 ([1,1,1], 0),
 ([0,0,0], 3),
 ([1],0),
 ([],-1),
 ([0]*100+[1]*200, 100)
 
]

# Function to invoke the test cases against the function that calculates the actual count of zeros. The actual count is compared with expected count for the 
# test casevalidation

def tester(test_cases):
 for test_case in test_cases:
  arr,expected = test_case
  actual = determine_count_of_zeros(arr)
  print("Testing: ", arr)
  if actual == expected:
   print("Success! ")
  else:
   print(f"Failed! Expected {expected} but got {actual}")


tester(test_cases)