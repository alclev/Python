import matplotlib.pyplot as plt
import math

x=[]
y=[]

i=0
while(i<=2*math.pi):
    x.append(i)
    y.append(math.sin(i))
    i+=0.01
    
plt.plot(x,y)

while (i<= 2* math.pi):
    x.append(i)
    y.append(0)
    i+=0.1
    
plt.xlabel('x')
plt.ylabel('y')



plt.title('Sin Wave')
#plt.legend()
plt.draw()
plt.show()
