'''
This program is used to implement the Normal Equation method in Linear Regression using scikit learn library. This approach is useful for dealing training dataset 
with the less number of features. The new weights or theta values are computed based on the input values of X and initial values of y (labels). The number of instances or rows considered can be varied. Also, the input values for prediction can be varied / provided to determine the labels based on the new computed weights/theta.

'''

from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# 100 x 1

X= 2*np.random.rand(100,1)

#theta_zero = 4.0
#theta_one = 3

y = 4 + 3*X + np.random.randn(100,1)


plt.plot(X,y,"b.")

plt.xlabel("$x_1$", fontsize=18)
plt.ylabel("$y$", rotation=0, fontsize=0)
plt.axis([0,2,0,15])
#plt.show()

 
# Compute theta or weights using Normal Equation Solution implemented through Scikit Learn Library


lin_reg = LinearRegression()

lin_reg.fit(X,y)

intercept  = lin_reg.intercept_
regression_co_eff = lin_reg.coef_


print("Theta Best Values/computed Weights are", intercept,regression_co_eff)



# Use Theta Best (New Weights) for Predicting any X vector containing values


list_input = []
list_input.append(0)
list_input.append(2)

X_new = np.array(list_input)

X1 = X_new.reshape(-1,1)     # One extra step is needed to change the input data for predicting the correct values

print("The dimension is ",X1.ndim)


#X1 =  np.array([[0],[2]])

print(X1)

y_pred = lin_reg.predict(X1)

print("The predicted value of Y Vector (ROWS) using new weights/theta best values is: ",y_pred)