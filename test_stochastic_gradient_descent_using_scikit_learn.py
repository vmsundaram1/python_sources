'''
This program contains the implementation of Stochastic Gradient Descent (SGD) using Scikit Learn approach where SGDRegressor is used as a linear model for training.
 

'''


from sklearn.linear_model import SGDRegressor
import numpy as np


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


# Logic for SGD using Scikit Learn library


theta = np.random.randn(2,1)			# Define and Initialize the values of weights/theta


#  Implementing SGD Using Scikit Learn library - EPOCH Loop for Stochastic Gradient Descent Computation and determination of new value of theta/weights


# Note max_iter and eta0 are the correct arguments used in the init method of the class. So, the arguments need to be passed correctly.

sgd_reg = SGDRegressor(max_iter=50, penalty=None, eta0=0.1)  	

sgd_reg.fit(X,y.ravel())

print("SGD Intercept = ",sgd_reg.intercept_,"SGD Co-efficient = ",sgd_reg.coef_)



# Use Theta Best (New Weights) for Predicting any X vector containing values


theta_best = np.array([sgd_reg.intercept_,sgd_reg.coef_])

print(theta_best)


list_input = []

list_input.append(0)
list_input.append(2)

length_of_input_x =  len(list_input)

X_new = np.array(list_input)

#X_new =  np.array([[0],[2]])

print(X_new)


# Predicting the final Value of Y vector based on test dataset values of X

X1 = X_new.reshape(-1,1)     # One extra step is needed to change the input data for predicting the correct values

y_pred = sgd_reg.predict(X1)


#X_new_b = np.c_[np.ones((length_of_input_x,1)),X_new]
#y_pred  =  X_new_b.dot(theta_best)


print("The predicted value of Y Vector (ROWS) using new weights/theta best values is: ",y_pred)




