import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7,8]
y=[1,3,6,3,5,5,3,6]

plt.scatter(x,y,label='skitscat', color='k', marker='x', s=100)

plt.xlabel('x')
plt.ylabel('y')
plt.title('ScatterPlot')
plt.legend()
plt.show() 
