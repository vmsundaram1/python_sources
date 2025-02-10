'''
This program is used to implement Gradient Descent implementation for fitting a straight for a given a random set of data points. It applies weights for slopes and intercept during each iteration and computes total squared error based on predicted values of weights during every iteration. The convergence is achieved based on the pre-set orders of magnitude for precision/accuracy levels.  

'''

from random import random
import matplotlib.pyplot as plt
import math

# A function definition to determine a given set of input data (X,Y) based on weights (slope and intercept) supplied as an argument parameter. The function returns
# a list of tuples containing points i.e -> x and y co-ordinates

def get_input_data(weights):

 X =[]
 Y =[]

 m_initial,c_initial = weights 

 for i in range(1,10):
  X.append(i)
  temp = 10*m_initial*i + c_initial*10 - 4*random()
  Y.append(temp)
  
 input_data = (X,Y)
 print(input_data[0],input_data[1])
 
 return input_data


# A function definition to plot a given list of tuples using matplotlib method call

def plot_data(inp):
 plt.scatter(inp[0],inp[1])


# The function definition computes squared error of predicted variable with its original value based on a given input data - weights and data points (x,y) 

def square_loss_func(weights,inp_tup):

 m_new,c_new = weights

 initial_x = list(inp_tup[0])
 initial_y = list(inp_tup[1])


 total_squared_error=0.0

 for i in range(len(initial_x)):

  y_predicted = initial_x[i]*m_new + c_new     

  val = y_predicted-initial_y[i]   

  total_squared_error+=val*val

 return total_squared_error


'''

This function definiton computes the differentiaton of a given function by applying delta and weights (slope, intercept) taking one of 
weights each time it is called.

'''

def differentiator_func(loss_func, weight, index, initial_input_tup):

 weights = weight.copy() 

 delta = 1e-5

 Y_error = loss_func(weights,initial_input_tup)

 weights[index]+= delta

 Y1_error = loss_func(weights,initial_input_tup)

 return (Y1_error-Y_error)/delta


# Main Program Starts for Gradient Descent Implementation

slope=random()
intercept=random()
eta=0.0001

weights = [slope,intercept]

# Predict the unknown variable using the method by passing weights as agrument parameter and get the output list containing data points in tuples

input_tup = get_input_data(weights)

print(input_tup)
#plot_data(input_tup)



# The program logic checks determines the squared error based on a method call and runs through a loop to check if both computed slope and intecept values 
#converge with their corresponding total squared error values converge within 4 orders of magnitude.

epoch=0
iteration_error_value=math.sqrt(square_loss_func(weights,input_tup))      			# Compute 2nd order error value based on weights and input data points
#iteration_error_value=square_loss_func(weights,input_tup)
iteration_error_value1=0.0
 

while(abs(iteration_error_value1-iteration_error_value) > 1e-7):
  epoch+=1
  if((epoch%1000)==0):								# Reducing the value of eta for every 1000 iterations
   eta = eta/10
  print(epoch,"Current Loss/Error: ",iteration_error_value, eta, weights)
  de_dm = differentiator_func(square_loss_func,weights,0,input_tup)		# Determine the 1st derivative of slope based on computed 2nd order error value
  de_dc = differentiator_func(square_loss_func,weights,1,input_tup)		# Determine the 1st derivative of slope based on computed 2nd order error value

  slope_new = slope - eta*de_dm				# Equation to determine new slope using old slope, learning rate and 1st derivative of slope
  intercept_new = intercept - eta*de_dc			# Equation to determine new intercept using old intercept, learning rate and 1st derivative of intercept

  slope,intercept = slope_new,intercept_new

  weights = [slope,intercept]				# Assign the new slope and new intercept to the weights before proceeding for next iteration

  iteration_error_value1=iteration_error_value
  iteration_error_value=math.sqrt(square_loss_func(weights,input_tup)) # Compute 2nd order error value based on new weights and input data points
#  iteration_error_value=square_loss_func(weights,input_tup)      
