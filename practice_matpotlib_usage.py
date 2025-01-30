from matplotlib import pyplot as plt

fig, ax = plt.subplots()             			      # Create a figure containing a single Axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3], [1, 0, 4, 3], [1,5,4,2])  # Plot some data on the Axes.
plt.show()                           		              # Show the figure.



x=[
   [0,2,1],
   [2,3,4],
   [4,5,6]
  ]

z=[
   [255,127,0],
   [255,0,127],
   [127,255,0],
   [0,127,255]
  ]

y=[
   [0,2,1,3,4,5,6,7],
   [2,3,4,8,7,5,1,2],
   [4,5,6,2,7,0,8,1]
  ]

plt.imshow(z)  						     # Show colorful plot
#plt.imshow(y,cmap="gray")				     # Show grayed scale plot



