'''
This program gives the implementation of Batch Gradient Descent Approach. The entire set of training data is used to train the model and arrive at the finalized weights. RMSE is used for computation of error. Using the theta best/final weights, the prediction is then done for the test data.

'''

import math
import numpy as np
import matplotlib.pyplot as plt


# A Function to determine Root Mean Squared Error(RMSE) or Loss with variable weights 

def determine_mse(X_b,y,theta):

 y_predicted = X_b.dot(theta)
  
 error = y_predicted - y

 sq_error = error*error

 loss = np.sum(sq_error,axis=0)

 return math.sqrt(loss)


# Initialize the values of X and determine the value of Y vector; 

X= 2*np.random.rand(100,1)

#theta_zero = 4.0
#theta_one = 3


y = 4 + 3*X + np.random.randn(100,1)


# Concatenate a vector containing value of 1 with the vector containing X data to form a matrix


X_b = np.c_[np.ones((100,1)),X]

print("X_b =",X_b)

print("Shape of X and Y are : ",X_b.shape,y.shape)


# Determine Transpose of Matrix X 

X_transpose = X_b.T



# Logic for Batch Gradient Descent

eta = 0.1					# Learning Rate

no_of_iterations =  1000			# Number of Iterations for reducing error and achieving convergence 

number_of_rows_m = 100				# Number of Instances or rows of data

theta = np.random.randn(2,1)			# Define and Initialize the values of weights/theta


#  EPOCH Loop for Gradient Descent Computation and determination of new value of theta/weights


for iteration in range(no_of_iterations):

 gradients = (2/number_of_rows_m) * X_transpose.dot( X_b.dot(theta) - y)

 theta = theta - eta * gradients

 error = determine_mse(X_b,y,theta)

 if(iteration % 50 == 0): 
  print("Count = ",iteration+1,"Loss/Error = ",error,"New Theta/Weights are:",theta)



# Use Theta Best (New Weights) for Predicting any X vector containing values


theta_best = theta


list_input = []

list_input.append(0)
list_input.append(2)

length_of_input_x =  len(list_input)

X_new = np.array(list_input)

#X_new =  np.array([[0],[2]])

print(X_new)


# New Method

X_new_b = np.c_[np.ones((length_of_input_x,1)),X_new]
y_pred  =  X_new_b.dot(theta_best)


print("The predicted value of Y Vector (ROWS) using new weights/theta best values is: ",y_pred)


