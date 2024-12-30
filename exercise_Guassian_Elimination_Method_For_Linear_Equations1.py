# This Python3 program is used to demonstrate working of Gaussian Elimination method using a class and its member variables, methods
# Also, this program builds a model by using sample data sets for training. By using the modelled equation, predicts the unknown value based on given any 
#random set of data

# Class Definition for a Linear Prediction Model

class linear_based_prediction_model:
  
 mat=[]  
 size_of_matrix=0
 result=[]

 def __init__(self,arr):
  
  self.size_of_matrix=int(len(arr[0]))-1
  self.mat=arr 
  self.result=[0]*self.size_of_matrix

 def get_Matrix(Self):  
  print(Self.size_of_matrix)
  for i in range(Self.size_of_matrix):
   print(Self.mat[i])  
#   for j in range(Self.size_of_matrix+1):
#    print(Self.mat[i][j])


# Function to reduce matrix to row echelon form (r.e.f.)

 def forwardElim(Self,mat):

    N=Self.size_of_matrix


    for k in range(N):
       
        # Initialize maximum value and index for pivot

        i_max = k

        v_max = mat[i_max][k]
 
        # find greater amplitude for pivot if any

        for i in range(k + 1, N):

            if (abs(mat[i][k]) > v_max):

                v_max = mat[i][k]
                i_max = i
 
        # if a principal diagonal element  is zero,
        # it denotes that matrix is singular, and
        # will lead to a division-by-zero later.

        if not mat[k][i_max]:
            return k    # Matrix is singular
 
        # Swap the greatest value row with current row

        if (i_max != k):
            Self.swap_row(mat, k, i_max)
 
        for i in range(k + 1, N):
 
            # factor f to set current row kth element to 0,
            # and subsequently remaining kth column to 0 */

            f = mat[i][k]/mat[k][k]
 
            # subtract fth multiple of corresponding kth
            # row element*/

            for j in range(k + 1, N + 1):
                mat[i][j] -= mat[k][j]*f
 

            # filling lower triangular matrix with zeros*/
            mat[i][k] = 0
 
        # print(mat);        //for matrix state
 
    # print(mat);            //for matrix state
    return -1         

# A Function Definition to get variable values/content using gaussian elimination method and calling backward substitution function on any given array/list
# of variable co-efficients

 def gaussianElimination(Self,mat,N):
 
    # reduction into r.e.f.

    singular_flag = Self.forwardElim(mat)
 
    # if matrix is singular

    if (singular_flag != -1):
 
        print("Singular Matrix.")
 
        # if the RHS of equation corresponding to
        #   zero row  is 0, * system has infinitely
        #   many solutions, else inconsistent*/

        if (mat[singular_flag][N]):
            print("Inconsistent System.")
        else:
            print("May have infinitely many solutions.")
 
        return
 
    # get solution to system and print it using
    #   backward substitution
    Self.backSub(mat)
 
# A Function definition for carrying out an Elementary Operation of Swapping two rows in any array/list of size N

 def swap_row(Self,mat, i, j):

    N=Self.size_of_matrix

    for k in range(N + 1):
 
        temp = mat[i][k]
        mat[i][k] = mat[j][k]
        mat[j][k] = temp
 

 
# Function to calculate the values of the unknowns and populate them in the member variable of the class 

 def backSub(self,mat):
  
    
    N=self.size_of_matrix

    x = [None for _ in range(N)]    # An array to store solution
 
    # Start calculating from last equation up to the
    #  first */
    for i in range(N-1, -1, -1):
 
        # start with the RHS of the equation */
        x[i] = mat[i][N]
 
        # Initialize j to i+1 since matrix is upper
        #  triangular*/
        for j in range(i + 1, N):
           
            # subtract all the lhs values
            # except the coefficient of the variable
            # whose value is being calculated */
            x[i] -= mat[i][j]*x[j]
 
        # divide the RHS by the coefficient of the
        #  unknown being calculated
        x[i] = (x[i]/mat[i][i])
        print("I am here",x[i])

 
    print("\nSolution for the system:")
    for i in range(N):
        print(i,"{:.8f}".format(x[i]))
        self.result[i]=x[i]

# A Function Definition to execute the forumulation of a model using equation/list co-efficients, values and returning the parameter values 
# in an 1D list.
 
 def fit_data_and_frame_linear_model(Self,arr):

  N=Self.size_of_matrix

  obj1.get_Matrix()

  obj1.gaussianElimination(arr,N)

  print("\nI am printing output vector")

  for i in range(N):
   print(round(obj1.result[i],4))

  return obj1.result


# A Function Definition to carry out the Prediction of the Unknown Parameter value based on the model equation and input data set of parameters.

 def predict_using_linear_model(Self,coords):

#  Self.result=r
  k = int(len(Self.result))
 
  var_unknown=0.0

  if(int(k)==int(len(coords)) and coords!=" "):
   for i in range(k):
    var_unknown+= float(Self.result[i])*float(coords[i])
    print("The temporary computed value is",var_unknown)
  else:
    raise Exception("THis is not correct data, Input Array Size Mismatch/Data Error, Prediction halted")

  return var_unknown

 def input_data_collection_for_prediction(Self):

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

   diff = len(Self.result)-len(dependant_values)

  if(diff>0):
   for i in range(diff):
    dependant_values.append(val)
    done=True
  elif(diff<0):
   print("Enter only value ",-diff,"less so that the input entries are",len(Self.result))
   done=False 

  return dependant_values

# A Function outside the class definition that collects the input dataset for Model Formulation

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

 
# Main Program - Execution of linear model formulation and prediction of unknown parameter using dependant value parameters 

res=[]

arr=formulate_dataset_for_model() # Function call to Formulate the Input Dataset consisting of linear equation co-efficients and R.H.S values

obj1=linear_based_prediction_model(arr) # Create instance of the class

res=obj1.fit_data_and_frame_linear_model(arr)  # Function Call to fit the input data set so as to determine the co-efficients and model the linear equation


# Invoking Input Function for Dependant paramter data collection and validation for Predicting Unknown Parameter

dep_parameter_values =  obj1.input_data_collection_for_prediction()


# Invoking Function Call to predict the unknown parameter value using dependant set of parameters available

unknown_var = obj1.predict_using_linear_model(dep_parameter_values) 
   
print("\nThe predicted value of Unknown parameter for the given set of dependant values",dep_parameter_values,"is: ",unknown_var)