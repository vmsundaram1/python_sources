'''
This program is used to implement the Normal Equation method in Linear Regression. It is useful for dealing with the less number of features. The new weights or theta
values are computed based on the input values of X and initial values of y (labels). The number of instances / rows considered can be varied. Also, the input values
for prediction can be varied / provided to determine the labels based on the new computed weights/theta.

'''

import numpy as np
import matplotlib.pyplot as plt

def determine_Y(X,w):

 number_of_rows = X.shape[0] 

 ones = np.ones((number_of_rows,1))
 X1 = np.hstack((X,ones))

 Y_rows = X1.dot(w)

 return Y_rows

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


# Compute theta or weights using Normal Equation methodology - inverse(X.T*X) * (X.T)*y


X_b = np.c_[np.ones((100,1)),X]

print("X_b =",X_b)

X_transpose = X_b.T

theta_best = np.linalg.inv(X_transpose.dot(X_b)).dot(X_transpose).dot(y)


print("Theta Best Values/computed Weights are", theta_best[0],theta_best[1])

print("Theta Best (computed Weights) - Vector (1D-Array) is", theta_best)





# Use Theta Best (New Weights) for Predicting any X vector containing values



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


# old method 

#theta_new  = theta_best.reshape(-1,1)
#y_pred = determine_Y(X_new,theta_new)


print("The predicted value of Y Vector (ROWS) using new weights/theta best values is: ",y_pred)