from random import random
import matplotlib.pyplot as plt
x_list=[]
y_list=[]

for x in range(0,25):
 y=4*x+10+(15*random())
 x_list.append(x)
 y_list.append(y)

plt.scatter(x_list,y_list)
plt.show()