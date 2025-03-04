'''
Gradient Descent Implementation using an utility class and a Regression Model class that uses the methods of the gradient descent utility class

This implementation uses NUMPY throughout and applies weights for features/characteristics during each iteration and computes mean squared error based on predicted values of weights during every iteration. The convergence is achieved based on the pre-set error criteria i.e error drops to certain specified orders of magnitude for precision/accuracy levels. 
The training data is computed with a specified number of instances/experiences that can be varied and the initial/actual values are computed accordingly. 

'''

import numpy as np
import math
from gradient_utilities import Gradient_Utils

'''
A regression model class definition that contains the essential methods required for implementing the gradient descent using NUMPY. It uses the methods/functions from Gradient_Utils class

'''


class MyRegressionModel():

 # Function to initialize the variables - constructor for the class

 def __init__(self,lossf=None,eta=0.001,delta=1e-2):
  self.weights = None
  if lossf is None:
   self.lossf = Gradient_Utils.mse_loss
  self.eta = eta
  self.delta=delta


 '''

 A function definition to determine a given set of input data (X,Y) based on weights (slope and intercept) supplied as an argument parameter. The function returns
 a list of tuples containing points i.e -> x and y co-ordinates

 '''

 def get_input_data(self,m,weights):

  number_of_rows=m						# Number of instances/experiences or data is taken as a constant for training purposes 
  number_of_features = weights.shape[0]-1
  print("TOTAL FEATURES and TOTAL WEIGHTS", number_of_features,weights.shape[0])

  X_rows = np.random.random((number_of_rows,number_of_features))

  Y = Gradient_Utils.determine_Y(X_rows,weights) + np.random.random((number_of_rows))*5 - 5*np.random.random((number_of_rows))

  input_data = (X_rows,Y.reshape(-1,1))				# Initial values of Y is re-shaped so that the loss computation can be done without failure
 
  return input_data


 # Function definition to initialize the weights/characteristics/features

 def __init_weights(self,n):
  np.random.seed(10)
  w = np.random.randint(10,200,n+1)
  return w


 # Function Definition to initialize the input data required for training the model


 def initialize_input_data(self,m,n):

  number_of_features = n
  weights = self.__init_weights(n) 
  input_tup = self.get_input_data(m,weights)
  self.weights=weights.reshape(1,-1)
  self.number_of_rows=m
  self.number_of_features=n
  
  return input_tup


 '''
 The fit method definition contains the program logic that checks the input data and determines the squared error based on methods from Gradient_Utils class and 
 runs through a loop to check if both computed weights/co-efficients converge with their corresponding mean squared error values below the specified orders of 
 magnitude i.e error.

 '''


 def fit(self,X,y):
 
  epoch=0
  eta=self.eta  
  if(self.weights.shape[0]!=0):
   print("The weights are already intialized", self.weights.shape[0],self.weights)
  else:
   self.__init_weights(n)

  iteration_error_value = self.lossf(X,y,self.weights)
  iteration_error_value = math.sqrt(iteration_error_value)
  iteration_error_value1=0.0

  deltas = Gradient_Utils.prepare_deltas(self.weights,self.delta)


  while(abs(iteration_error_value1 - iteration_error_value) > 1e-9):

   epoch+=1
   w = self.weights

#  if(epoch%1000==0):
#   eta = eta/10

   print(epoch,"Current Loss/Error: ",iteration_error_value1,eta,w)

   self.weights = Gradient_Utils.new_weights(X,y,w,eta,self.delta,deltas,self.lossf) 
   iteration_error_value1 = iteration_error_value
   iteration_error_value = self.lossf(X,y,self.weights)
   iteration_error_value = math.sqrt(iteration_error_value)


# Main Program Starts   

eta=0.001
delta=0.01
reg = MyRegressionModel(None,eta,delta)

# Specify number of sample input data (rows) and number of characteristics (features) to generate input data

number_of_rows = 10
number_of_features = 5
 
input_data = reg.initialize_input_data(number_of_rows,number_of_features)	         

reg.fit(input_data[0],input_data[1])

# Print the Final Output Data based on the Converged Value of Weights

final_Y  = Gradient_Utils.determine_Y(input_data[0],reg.weights)

print("The final value for weights are:", reg.weights)
print("The final value of Y vector is ",final_Y)
