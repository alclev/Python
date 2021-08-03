import matplotlib.pyplot as plt

days=[1,2,3,4,5]

working=[4,4,8,10,6]
eating= [9,18,9,3,4]
sleeping=[4,1,3,5,8] #each column adds up to the same thing
playing=[7,1,4,6,6]

plt.plot([],[], color='m', label='Working')
plt.plot([],[], color='c', label='Eating')
plt.plot([],[], color='b', label='Sleeping')
plt.plot([],[], color='r', label='Playing')

plt.stackplot(days, working, eating, sleeping, playing, colors=['m','c','b','r']) 

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('StackPlots')

plt.show()