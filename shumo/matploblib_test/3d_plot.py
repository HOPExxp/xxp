from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = Axes3D(fig)
X= np.arange(-4,4,0.25)
Y= np.arange(-4,4,0.25)
X,Y = np.meshgrid(X,Y)
R = np.sqrt(X**2+Y**2)
z = np.sin(R)
ax.plot_surface(X,Y,z,rstride=1,cstride=1,cmap='hot')
plt.show()