# This test program is used to carry out the Gradient Descent implementaiton for a simple linear equation -> y = 3x+2 using NUMPY

import numpy as np

X = np.array([ [1], [2], [3] ])

y = np.array([5.1, 7.9, 11.1])

weights = np.array([1,2])
old_weights = weights


def square_loss_func1(weights,inp_tup):

 initial_x = inp_tup[0]			# Actual value for x data containing tuples of features
 initial_y = inp_tup[1]			# Actual value for y data given as input after computation
 

 y_predicted = determine_Y(initial_x,weights)
 error = y_predicted - initial_y
 sq_error = error*error
 loss = np.sum(sq_error,axis=0)

 return loss


def determine_Y(X,w):

 number_of_rows = X.shape[0] 

 ones = np.ones((number_of_rows,1))
 X1 = np.hstack((X,ones))

 Y_rows = X1.dot(w.T)

 return Y_rows


def differentiator_func(loss_func, weight, initial_input_tup):

 weights = weight.copy() 

 delta = 0.01

 # Loss Before Increase in Weights

 previous_loss = square_loss_func1(weights,initial_input_tup)


 # Loss After Increase in Weights

 size_numw = weights.shape[-1]
 a = np.zeros((size_numw,size_numw))
 np.fill_diagonal(a,delta)
 new_weights = weights+a
 
 current_loss = square_loss_func1(new_weights,initial_input_tup)

 gradients = (current_loss-previous_loss)/delta 

 return gradients


y_pred = determine_Y(X,weights)
print("Y predicted is", y_pred)

diff = y_pred - y

print("The initial diff error is ", diff)
print("1st sum of all errors is ",np.sum(diff*diff))



delta = 0.01

w_new = np.array([[1+delta, 2], [1,2+delta]])

#print(w_new)

new_pred = determine_Y(X,w_new)

new_error = new_pred - y.reshape(-1,1)

print(new_error)


sq_error = new_error*new_error

print(sq_error)

loss = np.sum(sq_error,axis=0)

print(loss)


final_value = (loss-np.sum(diff*diff))/delta

print(final_value)

eta=0.01

weights =  weights - eta*final_value

print("the next set of weights is",	weights)




# Test the function

print("*********************************************************")
print("Testing Loss function and Differentiator Function")
print("*********************************************************")

input_tup = (X,y.reshape(-1,1))

weights=weights.reshape(1,-1)
old_weights=weights
eta=0.01

for i in range(5000):
 if(eta%1000==0):
  eta = eta/10

 initial_loss = square_loss_func1(old_weights,input_tup)

 print("epoch=",i+1,"Loss/Error=",initial_loss,"Weights=",old_weights)

 derivative_parameters = differentiator_func(square_loss_func1,old_weights,input_tup)

 weights = old_weights - eta*derivative_parameters

 old_weights = weights

