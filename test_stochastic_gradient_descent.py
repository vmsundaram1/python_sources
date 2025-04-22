'''

This program contains the Stochastic Gradient Descent(SGD) Implementation. This approach considers only 1 instance/row of training input dataset for computing gradients in every iteration. It incorporates a learning schedule for determining learning rate (eta) during the determination of weights/theta values for different iterations. Also, the error is computed for every iteration using RMSE and it gives a measure of a convergence of the solution. 

'''

import math
import numpy as np
import matplotlib.pyplot as plt


def learning_schedule(t,t0,t1):

 return t0/(t+t1)

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
print("length of X_b =",len(X_b))

print("Shape of X and Y are : ",X_b.shape,y.shape)

# Determine Transpose of Matrix X 

X_transpose = X_b.T



# Logic for Batch Gradient Descent

#eta = 0.1					# Learning Rate

no_of_iterations =  50				# Number of Iterations for reducing error and achieving convergence 

t0,t1 = 5,50					# Learning SChedule Hyper Parameters

number_of_rows_m = 100				# Number of Instances or rows of data

theta = np.random.randn(2,1)			# Define and Initialize the values of weights/theta

theta_path_sgd=[]


#  EPOCH Loop for Stochastic Gradient Descent Computation and determination of new value of theta/weights



for iteration in range(no_of_iterations):
 
 for i in range(number_of_rows_m):

#  if epoch == 0 and epoch < 20:
#   y_predict = X_new_b.dot(theta)
#   style = "b-" if iteration > 0 else "r--"
#   plt.plot(X_new, y_predict, style)

  
  random_index = np.random.randint(number_of_rows_m)
  
  xi = X_b[random_index:random_index+1]
  yi = y[random_index:random_index+1]

  gradients = 2*xi.T.dot( xi.dot(theta) - yi )

  eta = learning_schedule(iteration*number_of_rows_m+i,t0,t1)
  
  theta = theta - eta * gradients

  theta_path_sgd.append(theta)
  
 error = determine_mse(X_b,y,theta)

# if(iteration % 50 == 0): 
 print("Count = ",iteration+1,"Loss/Error = ",error,"New Theta/Weights are:",theta,"Eta = ",eta)



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
