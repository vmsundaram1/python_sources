'''
This program is used to sort the list containing tuples using the Counting Sort Algorithm.

O(N+M), where N and M are the size of inputArray[] and countArray[] respectively. 

'''

# Function Call to implement the Counting Sort Algorithm

def sorting_tuples(input_array):

    # Finding the maximum element of input_array.

#    M = int(max(input_array))

    # Create a temporary list for holding the value on the 1st element of the tuple.

    temp_list=[]
    for i in range(len(input_array)):
     temp_list.append(int(input_array[i][0]))
   
    M=int(max(temp_list))
    print(M)
    print(temp_list)

    # Initializing count_array with 0

    count_array = [0] * (M + 1)


    # Mapping each element of temp_list (1st element of each tuple in the input_array) as an index of count_array

#    for num in input_array:

    for num in temp_list: 
        count_array[num] += 1

    print(count_array)

    # Calculating prefix sum at every index of count_array

    for i in range(1, M + 1):
        count_array[i] += count_array[i - 1]

    print(count_array)

    # Creating output_array from count_array

    output_array = [0] * len(input_array)

    for i in range(len(input_array)-1, -1, -1):
        print(temp_list[i],input_array[i][1])

        output_array[count_array[temp_list[i]]- 1] = (temp_list[i],input_array[i][1])

#        count_array[input_array[i][0]] -= 1

        count_array[temp_list[i]]-=1

    return output_array



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


# Function call to sort list containing tuples and print the sorted output data

result = sorting_tuples(input_list)

print("The sorted output using the conventional method of sorting is ",result)