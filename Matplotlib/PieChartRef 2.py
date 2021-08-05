import matplotlib.pyplot as plt

#days=[1,2,3,4,5]

#working=[4,4,8,10,6]
#eating= [9,18,9,3,4]
#sleeping=[4,1,3,5,8] #each column adds up to the  24 hours
#playing=[7,1,4,6,6]

slices=[3,8,14,4]

activities=['sleeping','eating','working','playing']
cols=['c','m','r','b']
plt.pie(slices, labels=activities, colors=cols, startangle=90, shadow=True, explode=(0,0.1,0,0), autopct='%1.1f%%')

plt.title('PieChart')

plt.show()