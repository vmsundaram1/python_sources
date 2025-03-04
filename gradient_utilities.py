import numpy as np
import math

# Gradient Utility Class defined with generic methods that can be used in the models.

class Gradient_Utils():


 # The Loss function definition computes squared error of predicted variable with its original value based on a given input data - weights and data points (x,y) 

 def mse_loss(initial_x,initial_y,weights):

  y_predicted = Gradient_Utils.determine_Y(initial_x,weights)

  error = y_predicted - initial_y

  sq_error = error*error

  loss = np.sum(sq_error,axis=0)

  return loss


 '''

  The Function Definition is used to prepare the formation of incremental weights during every iteration and subsequently used in the Graident Computation.
  The incremental matrix is prepared separately so as to avoid repeated calculation each time.

 '''

 def prepare_deltas(weights,delta):
  
  size_numw = weights.shape[-1]
  a = np.zeros((size_numw,size_numw))
  np.fill_diagonal(a,delta)
 
  return a


 '''

 This function definiton computes the differentiaton of a given function/gradients by applying delta and weights (slope, intercept) taking all incremental weights 
 at the same time when it is invoked/called for execution.

 '''
  

 def differentiator_func_to_compute_grad(X,y,w,delta,deltas,lossf):

  w1 = w.copy() 

  # Loss Before Increase in Weights

  previous_loss = lossf(X,y,w1)

  # Lose After Increase in Weights

  new_weights = w1+deltas
 
  current_loss = lossf(X,y,new_weights)

  gradients = (current_loss-previous_loss)/delta

  return gradients


 # Function Definition to compute new weights by using the method to evalutate gradients of each of the weights and mse error

 def new_weights(X,y,w,eta,delta,deltas,lossf):

  derivative_parameters = Gradient_Utils.differentiator_func_to_compute_grad(X,y,w,delta,deltas,lossf)
  w_new = w - eta*derivative_parameters

  return w_new



 # A Function to determine the values for Y by performing a scalar dot product of X-Co-ordinate Array and transpose of Weights Vector.

 def determine_Y(X,w):

  number_of_rows = X.shape[0] 

  ones = np.ones((number_of_rows,1))
  X1 = np.hstack((X,ones))

  Y_rows = X1.dot(w.T)

  return Y_rows

