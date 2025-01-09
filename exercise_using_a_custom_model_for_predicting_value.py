'''
 This program is used to arrive at a standard prediction model that can be utilized to compute unknown variable based on a dependent variable
 An equation of third order is employed to arrive at the predicted value. 
 For a given range of values of X, the values of Y are predicted and populated in the result array of the Class 
'''

# A class definition containing the dependant variable/co-ordinate, size of the 1D-array and the result as variables. Member methods are defined for constructor
# and a custom model for prediction

class prediction_model_equation:

 size_of_arr=0 
 co_orinates=[]
 result=[]  

 def __init__(self,coord_list):
  self.size_of_arr = int(len(coord_list))
  self.co_ordinates=coord_list
  self.result=[0]*(int(len(coord_list)))

# The custom model is based on a third order equation that is used to predict the value of unknown variable Y[i] based on a given range of X values - X[i]

 def predict_using_custom_model(self,coords):
  if(int(self.size_of_arr)!=0 and coords!=""):
   i=0
   for i in range(self.size_of_arr):
    temp_x= float(coords[i])
    temp_y_val= 1*(temp_x**3) + 10*(temp_x**2)+ (10**2)*(temp_x) + 10**3
    self.result[i] = temp_y_val
   return True
  else:
   raise Exception("THis is not correct data, Input Array Size Mismatch/Data Error, Prediction halted")
   return False 


# Input Data Collection

Array1 = input("Enter the dependant variable values separated by Commas\n")

coord_x_list = Array1.split(',')


# Class Instantiation and FUnction Call to Predict using the Value


obj_model = prediction_model_equation(coord_x_list)

bool_temp = obj_model.predict_using_custom_model(coord_x_list)




print(bool_temp)

# Printing the Dependant Variable and the Predicted Value

if(bool_temp==True):
 for i, val in enumerate(obj_model.result):
  print("The output value as predicted by the model for the dependant variable",coord_x_list[i],"is",val)