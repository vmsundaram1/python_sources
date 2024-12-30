import math

class line_Eqn:
    
 def __init__(Self):
  Self.m = 0
  Self.c = 0
 
 def getM_value(Self):
  x=Self.m
  return x

 def getC_value(Self):
  x=Self.c
  return x

 def determine_length(Self,X,Y):

  x1,x2 = X
  y1,y2 = Y

  x_sqr =  (x1-x2)**2
  y_sqr =  (y1-y2)**2

  distance = float(math.sqrt(x_sqr+y_sqr))

  print("The length between two points is", distance)


  return distance

 def calculate_distance(Self,XY_Data):

  x1,y1 = XY_Data[0]
  x2,y2 = XY_Data[1]

  x_sqr =  (x1-x2)**2
  y_sqr =  (y1-y2)**2

  distance = float(math.sqrt(x_sqr+y_sqr))

  print("The calculated distance is", distance)

  return distance

# Take the dataset consisting of separate Arrays of X,Y co-ordinates and determine the model equation      

 def fit_line_model(Self,X,Y):
  x1,x2=X
  y1,y2=Y
     
  Self.m = (y2-y1)/(x2-x1)
  Self.c =  (x2*y1-x1*y2)/(x2-x1)


# Take the dataset consisting of Single Array of X,Y points, expressed as tuples and determine the model equation     

 def fit_line_model_second_variation(Self,XY_Data):
 
  x1,x2=XY_Data[0][0],XY_Data[1][0]
  y1,y2=XY_Data[0][1],XY_Data[1][1]
     
  Self.m = (y2-y1)/(x2-x1)
  Self.c =  (x2*y1-x1*y2)/(x2-x1)

# Predict the value of Y for a given value of X
  
 def predict_Y(Self,x):
   y = x*Self.m + Self.c
   return y


x_arr=[1,2]

y_arr=[3,5]

xy=[(1,3),(2,5)]


#input("Enter the input values of the X co-ordinates, separated by commas:"\n);
#input("Enter the input values of the y-co-ordinates, separated by commas:\n")


obj_line_eqn = line_Eqn()

print("The INITIAL value of Slope M is :",obj_line_eqn.m)
print("The INITIAL value of Constant C is :",obj_line_eqn.c)

dist = obj_line_eqn.determine_length(x_arr,y_arr)

dist2 = obj_line_eqn.calculate_distance(xy)

if(dist==dist2):
 print("Both functions are working!")

obj_line_eqn.fit_line_model(x_arr,y_arr)

#obj_line_eqn.fit_line_model_second_variation(xy)


print("The FINAL value of Slope M is :",obj_line_eqn.m)
print("The FINAL value of Constant C is :",obj_line_eqn.c)

x1=[1,2,3,4,5]

for i in range(int(len(x1))):
 y = obj_line_eqn.predict_Y(x1[i])
 print("The value of Y in case of X=",x1[i],"is: ",y)
