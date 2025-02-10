'''
This generic program is used to implement Gradient Descent implementation for fitting a straight for a given a random set of data points representing multiple features. 
It applies weights for slopes and intercept during each iteration and computes total squared error based on predicted values of weights during every iteration. The convergence is achieved based on the pre-set orders of magnitude for precision/accuracy levels. 

The training data is computed with a specified number of instances/experiences that can be programmatically varied and the initial/actual values are computed 
accordingly. 

'''

from random import random
import matplotlib.pyplot as plt
import math

# A function definition to determine a given set of input data (X,Y) based on weights (slope and intercept) supplied as an argument parameter. The function returns
# a list of tuples containing points i.e -> x and y co-ordinates

def get_input_data(weights):

 X =[]
 Y =[]

 number_of_rows=25						# Number of instances/experiences or data is taken as a constant for training purposes 
 features = len(weights)
 temp=[0]*(len(weights)-1)


# Taking the intercept parameter out from weights


 intercept_c = weights[len(weights)-1]

 print("The intercept is :",intercept_c)


# Setting the Value of Feature Parameters - Actual values of X data for training
 
 for k in range(number_of_rows):
  for i in range(len(weights)-1):
   temp[i]=i*random()
  X.append(tuple(temp))
   
 temp=0.0

 

# Setting the value of Label / Target Parameter - Actual Values of Y data for traning

 x_val = tuple() 
 for i in range(number_of_rows):
  temp = intercept_c*10
  x_val=X[i]
  for j in range(len(weights)-1):
   temp+= 10*weights[j]*int(x_val[j])
  Y.append(temp)

 
 input_data = (X,Y)
 
 return input_data


# A function definition to plot a given list of tuples using matplotlib method call

def plot_data(inp,weights):

 print("I am inside plot data:", len(inp), len(inp[0]),len(inp[1]))

 X_data = inp[0] 
 plot_X = [0]*len(inp[1])
 X = []

 for i in range(len(weights)-1):
  temp = list(map(lambda x:x[i],X_data))
  X.append(temp)
  print("Inside Loop", X)
  plt.scatter(X[i],inp[1])
"""
  fig, ax = plt.subplots()   
  ax.plot(X[i],inp[1])
  plt.show()
"""

# The function definition computes squared error of predicted variable with its original value based on a given input data - weights and data points (x,y) 

def square_loss_func(weights,inp_tup):

 weight_length = len(weights)			
 initial_x = list(inp_tup[0])			# Actual value for x data containing tuples of features
 initial_y = list(inp_tup[1])			# Actual value for y data given as input after computation

 y_predicted = 0.0
 total_squared_error=0.0
 length = len(inp_tup[1])

 for i in range(length):

  y_predicted = weights[weight_length-1]
  
  mytup = initial_x[i]

  temp = 0.0

  for j in range(weight_length-1):
   temp+= mytup[j]*weights[j]

   y_predicted= y_predicted + temp      

  val = y_predicted-initial_y[i]

  total_squared_error+=val*val
   
 return total_squared_error


'''

This function definiton computes the differentiaton of a given function by applying delta and weights (slope, intercept) taking one of 
weights each time it is called.

'''

def differentiator_func(loss_func, weight, index, initial_input_tup):

 weights = weight.copy() 

 delta = 1e-5

 Y_error = loss_func(weights,initial_input_tup)			# loss_func invokes the actual funcion square_loss_func defined in this program

 weights[index]+= delta

 Y1_error = loss_func(weights,initial_input_tup)		# loss_func invokes the actual funcion square_loss_func defined in this program

 return (Y1_error-Y_error)/delta



# Main Program Starts for Gradient Descent Implementation

weights = []

number_of_features = 5						# Set the input number of features to experiment with different input data variable combinations
 

# One additional entry for intercept/constant is also taken into account along with other weights/co-efficients

for i in range(number_of_features+1):
 temp = 1.5*random()
 weights.append(temp)

print("In Main", len(weights), weights)

input_tup = get_input_data(weights)

print("\n\n\nThe input data is ", input_tup)

print("\n\n\nThe weights is ", weights)

#plot_data(input_tup,weights)


# Learning Rate Variable can be set depending on the error trend observation

eta=0.0001


'''
The program logic checks determines the squared error based on a method call and runs through a loop to check if both computed slope and intecept values 
converge with their corresponding total squared error values converge within 4 orders of magnitude.

'''

epoch=0
iteration_error_value=math.sqrt(square_loss_func(weights,input_tup))      			# Compute 2nd order error value based on weights and input data points
#iteration_error_value=square_loss_func(weights,input_tup)
iteration_error_value1=0.0


weight_length = len(weights)
derivative_parameter = [0]*len(weights)
old_weights = [0]*len(weights)

while(abs(iteration_error_value1-iteration_error_value) > 1e-7):

 epoch+=1
 if((epoch%1000)==0):								# Reducing the value of eta for every 1000 iterations
  eta = eta/10
 print(epoch,"Current Loss/Error: ",iteration_error_value,eta,weights)
 i=0
 k=0
 for i in range(weight_length):				             # Determine the 1st derivative for the computed 2nd order error value based on all weights
  derivative_parameter[i] = differentiator_func(square_loss_func,weights,i,input_tup)	# Passing index for each weight parameter for computing corresponding derivative
 for k in range(weight_length):
  old_weights[k]=weights[k]
  weights[k] = weights[k]-eta*derivative_parameter[k]		# Equation to determine new weights using old values, learning rate and 1st derivative of error

 iteration_error_value1=iteration_error_value
 iteration_error_value=math.sqrt(square_loss_func(weights,input_tup))      # Compute 2nd order error value based on new weights and input data points
# iteration_error_value=square_loss_func(weights,input_tup)      # Compute 2nd order error value based on new weights and input data points



