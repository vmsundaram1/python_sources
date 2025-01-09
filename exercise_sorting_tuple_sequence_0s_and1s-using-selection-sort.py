'''
This program does the sorting of a set of tuples based on the first element of the tuples and returns the final result in an array.
The procedure involves the checking of first element of the tuple in each entry of the list and returns the sorted array/list
The order of complexity is O(n*n)

'''

# The function definition contains the sorting procedure by taking a list of tuples as an input and returns the result in the form of array/list.
# The function checks the value of the 1st element in each tuple and uses the same for sorting. The final result is returned as a list containing the sorted tuples.



def sorting_tuples(input_data_list):
 
 length = len(input_data_list)
 i=0

 for i in range(0,length):
  for j in range(i+1,length):
   term1 = input_data_list[i][0]
   term2 = input_data_list[j][0]
   if(term1 > term2):
    input_data_list[i],input_data_list[j] = input_data_list[j],input_data_list[i]

 return input_data_list


# Main Program Starts

# Sample Input Data

#input_list = [(0,'s'),(1,123),(1,"abc"),(0,"RTA"),(0,9087),(1,"5")]
#input_list = [(0,'bert'),(1,8),(1,"10"),(0,4),(0,"python"),(1,"eight"),(0,'five')]

# Input Data Collection

input_tup_list = eval(input("Enter the list of tuples with each tuple enclosed within parentheis and each tuple separated by commmas:\n"))	

input_list=[]
input_list = list(input_tup_list)
length = len(input_list)

print(length)
print(input_list)

# Function call to sort list containing tuples and print the sorted output data

result = sorting_tuples(input_list)

print("The sorted output using the conventional method of sorting is ",result)

