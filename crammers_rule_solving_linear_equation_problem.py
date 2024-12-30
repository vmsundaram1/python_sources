'''
This program determines the values of unknown variables based on the Crammer's rule. The constraint for this rule in determining the model parameters of linear

equation is that the determinant of the matrix of leading co-efficients should NOT be zero. In all other cases, the solution vector containing the unknown values

can be computed based on the input data set. 
 
''' 

# A Function Definition to compute the determinant of a given array using recursive calls till the array size is reduced to 2x2

def getDet(mat, n):
  
# Base case: if the matrix is 1x1
 if n == 1:
  return mat[0][0]
    
# Base case for 2x2 matrix
 if n == 2:
  return mat[0][0] * mat[1][1] - \
  mat[0][1] * mat[1][0]
    
# Recursive case for larger matrices
 res = 0
 for col in range(n):
      
# Create a submatrix by removing the first row and the current column
  sub = [[0] * (n - 1) for _ in range(n - 1)]

  for i in range(1, n):
   subcol = 0
   for j in range(n):
			# Skip the current column
    if j == col:
     continue            
                # Fill the submatrix
    sub[i - 1][subcol] = mat[i][j]
    subcol += 1
        
# Cofactor expansion
  sign = 1 if col % 2 == 0 else -1
  res += sign * mat[0][col] * getDet(sub, n - 1)
    
 return res


# The Swap Function definition contains the swapping of any two columns in any array

def swap_array_columns(arr,j,k):

 N = int(len(arr))
 for row in range(N):
  temp = arr[row][j]
  arr[row][j]=arr[row][k]
  arr[row][k]=temp

 return arr


def formulate_dataset_for_model():  
 N = input("Enter the size of the problem: \n")
 N=int(N)
 arr1=[]
 i=0
 done=False
 while not done:
  while i < N: 
   temp_list = input("Enter the row "+str(i+1)+" co-efficients for "+str(N)+" sized array, followed by the R.H.S value. Separate each of your entries by commas\n")
   actual_input=temp_list.split(",")
   if(len(actual_input)!=(N+1)):
    print("You have to re-enter the input data correctly to match the number of elements\n")
    done=False
    continue
   else:
    arr1.append(actual_input)
    i+=1
    done=True

 for i in range(N):
  for j in range(N+1):
   arr1[i][j]=float(arr1[i][j])   
   
 return arr1

def input_data_collection_for_prediction(resultant_vector):

  done=False
  while not done:
   multiple_values=input("Enter DEPENDANT PARAMETER VALUES, separated by commmas for predicting the UNKNOWN PARAMETER using the MODEL:\n")
   length_values = int(len(multiple_values))
   if(length_values > 1):
    dependant_values=multiple_values.split(",")
    done=True
   else:
    print("Error in Data Entry! Enter the Input Data again\n") 
    done=False
    continue

   val=0
   print("The Dependant Values are:",dependant_values)

   diff = len(resultant_vector)-len(dependant_values)

  if(diff>0):
   for i in range(diff):
    dependant_values.append(val)
    done=True
  elif(diff<0):
   print("Enter only value ",-diff,"less so that the input entries are",len(resultant_vector))
   done=False 

  return dependant_values



def predict_using_linear_model(result_values,coords):

 k = int(len(result_values))
 var_unknown=0.0

 if(int(k)==int(len(coords)) and coords!=" "):
  for i in range(k):
   var_unknown+= float(result_values[i])*float(coords[i])
   print("The temporary computed value is",var_unknown)
 else:
  raise Exception("THis is not correct data, Input Array Size Mismatch/Data Error, Prediction halted")

 return var_unknown

# Sample Data

mat1 = [ 
 	[1,2,3,4],
	[2,3,4,5],
 	[3,4,5,6]
      ]

mat2 = [ [3.0, 2.0, -4.0, 3.0], 
        [2.0, 3.0, 3.0, 15.0], 
        [5.0, -3, 1.0, 14.0]
      ]


# Main Program Starts

# Function call to Formulate the Input Dataset consisting of linear equation co-efficients and R.H.S values

mat=formulate_dataset_for_model() 

# Computation of Determinant of the N-sized array and using the same to solve the linear equations

print(int(len(mat)))

main_determinant = getDet(mat,int(len(mat)))

print("The determinant of the input matrix is :",round(float(main_determinant),4))

N = int(len(mat))

# The 1D vector of determinant is determined and used for computing unknown variables using Crammer's Rule

vector_determinant=[0]*N
resultant_value=[0.0]*N


''' 

By doing a column-swap of the augmented linear equation value (R.H.S part) with the column vector containing the co-efficients of unknown variable and computing the corresponding determinant, Crammer's rule can be applied. 

NOTE:-The determinant of original matrix should not be ZERO for crammers rule to be applicable.

'''

for i in range(N):
 res = swap_array_columns(mat,i,N)     
 print("The array after column swap is:",res)
 vector_determinant[i] = getDet(res,N)
 mat=swap_array_columns(res,N,i)
 print("The array after column swap is:",mat)
 if main_determinant!=0.0:
   resultant_value[i]=float(vector_determinant[i])/float(main_determinant) 
 else:
   print("The determinant of the original input array is zero and so it cannot be used to compute "+str(i)+"th variable value\n")
 print("The final values of the unknown variable: ",str(i),resultant_value[i])   


print("The final values of the unknown variables are: ",resultant_value) 


# Using the above Modelled Linear Equation, input data is collected on the dependant variables to predict the unknown variable


dependant_parameter_values=input_data_collection_for_prediction(resultant_value)


unknown_var=predict_using_linear_model(resultant_value,dependant_parameter_values)

print("\nThe predicted value of Unknown parameter for the given set of dependant values",dependant_parameter_values,"is: ",unknown_var)