from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = Axes3D(fig)
X= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]
Y= [2005,2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016]
X,Y = np.meshgrid(X,Y)
R = np.sqrt(X**2+Y**2)
z = np.sin(R)
ax.plot_surface(X,Y,z,rstride=1,cstride=1,cmap='hot')
plt.show()