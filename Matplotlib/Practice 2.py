import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA
import numpy as np
import math

x=[]
y=[]

i=0
#while(i<=2*math.pi):
#    x.append(i)
#    y.append(math.sin(i))
#    i+=0.001
    
#plt.plot(x,y)

while (i<= 2* math.pi):
    x.append(i)
    y.append(0)
    i+=0.1
    
plt.xlabel('x')
plt.ylabel('y')

ax = host_subplot(111, axes_class=AA.Axes)
xx = np.arange(0, 2*np.pi, 0.01)
ax.plot(xx, np.tan(xx))
ax.plot(x,y)

ax2 = ax.twin()  # ax2 is responsible for "top" axis and "right" axis
ax2.set_xticks([0., .5*np.pi, np.pi, 1.5*np.pi, 2*np.pi])
ax2.set_xticklabels(["$0$", r"$\frac{1}{2}\pi$",
                     r"$\pi$", r"$\frac{3}{2}\pi$", r"$2\pi$"])

ax2.axis["right"].major_ticklabels.set_visible(False)
ax2.axis["top"].major_ticklabels.set_visible(True)

#plt.title('Sin Wave')
#plt.legend()
plt.draw()
plt.show()