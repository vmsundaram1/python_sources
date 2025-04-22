'''
This program takes the given training data set and converts into a polynomial data as part of pre-processing before training a linear model. The weights are then determined using Linear Regression model and used for predicting values based on test data. 

'''

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import numpy as np
import math


# Initialize the values of X and determine the value of Y vector; 

m = 100

X = 6*np.random.rand(m,1)-3

y = 0.5*(X**2) + X + 2 + np.random.randn(m,1)


# Create the Polynomial 

poly_features = PolynomialFeatures(degree=2,include_bias=False)

X_poly = poly_features.fit_transform(X)

print(X[0])

print(X_poly[0])


# Logic for Polynomial Regression using Scikit Learn library - Linear Regression Model


lin_reg = LinearRegression()

lin_reg.fit(X_poly,y)

intercept  = lin_reg.intercept_
regression_co_eff = lin_reg.coef_


print("Theta Best Values/computed Weights are", intercept,regression_co_eff)




# Use Theta Best (New Weights) for Predicting any X vector containing values


#theta_best = np.array([intercept,regression_co_eff])

#print(theta_best)

list_input = []

list_input.append(0)
list_input.append(2)

length_of_input_x =  len(list_input)

X_new = np.array(list_input)

#X_new =  np.array([[0],[2]])

print(X_new)


# Predicting based on Polynomial Regression

X1 = X_new.reshape(-1,1)     # One extra step is needed to change the input data for predicting the correct values

poly_features = PolynomialFeatures(degree=2,include_bias=False)

X_poly_new = poly_features.fit_transform(X1)

y_pred = lin_reg.predict(X_poly_new)

print("The predicted value of Y Vector (ROWS) using new weights/theta best values is: ",y_pred)


