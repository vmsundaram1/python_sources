'''
This generic program is used to implement Gradient Descent implementation for fitting a straight line with a given a random set of data points representing multiple features/characteristics. This implementation uses NUMPY throughout and applies weights for slopes and intercept during each iteration and computes total squared error based on predicted values of weights during every iteration. The convergence is achieved based on the pre-set orders of magnitude for precision/accuracy levels. 
The training cdata is computed with a specified number of instances/experiences that can be programmatically varied and the initial/actual values are computed 
accordingly. 

'''

from random import random
import matplotlib.pyplot as plt
import math
import numpy as np

# A Function to determine the values for Y by performing a scalar dot product of X-Co-ordinate Array and transpose of Weights Vector.

def determine_Y(X,w):

 number_of_rows = X.shape[0] 

 ones = np.ones((number_of_rows,1))
 X1 = np.hstack((X,ones))

 Y_rows = X1.dot(w.T)

 return Y_rows



# A function definition to determine a given set of input data (X,Y) based on weights (slope and intercept) supplied as an argument parameter. The function returns
# a list of tuples containing points i.e -> x and y co-ordinates

def get_input_data(weights):

 number_of_rows=10						# Number of instances/experiences or data is taken as a constant for training purposes 
 number_of_features = weights.shape[0]-1
 print("TOTAL FEATURES and TOTAL WEIGHTS", number_of_features,weights.shape[0])

 X_rows = np.random.random((number_of_rows,number_of_features))

 Y = determine_Y(X_rows,weights) + np.random.random((number_of_rows))*5 - 5*np.random.random((number_of_rows))

 input_data = (X_rows,Y.reshape(-1,1))				# Initial values of Y is re-shaped so that the loss computation can be done without failure
 
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

 initial_x = inp_tup[0]			# Actual value for x data containing tuples of features
 initial_y = inp_tup[1]			# Actual value for y data given as input after computation
 

 y_predicted = determine_Y(initial_x,weights)

 error = y_predicted - initial_y

 sq_error = error*error

 loss = np.sum(sq_error,axis=0)

 return loss

'''

This function definiton computes the differentiaton of a given function/gradients by applying delta and weights (slope, intercept) taking all incremental weights 
at the same time when it is invoked/called for execution.

'''

def differentiator_func(loss_func, weight, initial_input_tup):

 weights = weight.copy() 

 delta = 0.01

 # Loss Before Increase in Weights

 previous_loss = square_loss_func(weights,initial_input_tup)

 # Lose After Increase in Weights

 size_numw = weights.shape[-1]
 a = np.zeros((size_numw,size_numw))
 np.fill_diagonal(a,delta)
 new_weights = weights+a
 
 current_loss = square_loss_func(new_weights,initial_input_tup)

 gradients = (current_loss-previous_loss)/delta 

 return gradients



# Main Program Starts for Gradient Descent Implementation


number_of_features = 5						# Set the input number of features to experiment with different input data variable combinations
 

# One additional entry for intercept/constant is also taken into account along with other weights/co-efficients

np.random.seed(10)

weights = np.random.randint(10,200,number_of_features+1)

input_tup = get_input_data(weights)

print("\n\n\nThe input data is ", input_tup)

print("\n\n\nThe weights is ", weights)

#plot_data(input_tup,weights)


# Learning Rate Variable can be set depending on the error trend observation

eta=0.001


'''
The program logic checks determines the squared error based on a method call and runs through a loop to check if both computed slope and intecept values 
converge with their corresponding total squared error values converge within 4 orders of magnitude.

'''

epoch=0

# Weights are reshaped so that broadcasting issues on the lines of different dimensions can be averted

weights = weights.reshape(1,-1)

iteration_error_value = square_loss_func(weights,input_tup)

print("The iteration value is ",iteration_error_value)

iteration_error_value = math.sqrt(iteration_error_value)

iteration_error_value1=0.0


while(abs(iteration_error_value1 - iteration_error_value) > 1e-9):

#for i in range(1000):

 epoch+=1
# if(epoch%1000==0):
#  eta = eta/10
 print(epoch,"Current Loss/Error: ",iteration_error_value1,eta,weights)
 
 derivative_parameters = differentiator_func(square_loss_func,weights,input_tup)
 weights = weights - eta*derivative_parameters


 iteration_error_value1=iteration_error_value
 iteration_error_value = square_loss_func(weights,input_tup)
 iteration_error_value = math.sqrt(iteration_error_value)


# Predicting the Final Output Value (Y) based on the converged value of Final Weights/Features/Characteristics

final_Y  = determine_Y(input_tup[0],weights)

print("The final value for weights are:", weights)
print("The final value of Y vector is ",final_Y)
