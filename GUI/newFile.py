from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)

fig = plt.figure(facecolor='xkcd:grey')
ax = fig.add_subplot(111, projection='3d')
ax.set_facecolor('xkcd:grey')

# x =[1,2,3,4,5,6,7,8,9,10]
# y =[5,6,2,3,13,4,1,2,4,8]
# z =[2,3,3,3,5,7,9,11,9,10]

x = [4.542239785,8.941687139,6.069811259,3.309678808,7.917407072]
y = [3.785100660,4.224900914,4.714002905,6.675400922,4.071284793]
z = [8.064804442,1.482040275,6.398090959,6.669711291,4.554042746]


ax.scatter(0, 0, 0, s=100, c='#A00000', marker='^')
ax.scatter(x, y, z, s=50, c='grey')
ax.plot3D([x[0],x[3]], [y[0],y[3]], [z[0],z[3]], linestyle='--', c='grey')
ax.plot3D([x[0],x[2]], [y[0],y[2]], [z[0],z[2]], linestyle='--', c='grey')
ax.plot3D([x[4],x[2]], [y[4],y[2]], [z[4],z[2]], linestyle='--', c='grey')
ax.plot3D([x[4],x[1]], [y[4],y[1]], [z[4],z[1]], linestyle='--', c='grey')
ax.scatter(x[3], y[3], z[3], s=60, c='green')

a = Arrow3D([0,3], [0,7], 
            [0,6], mutation_scale=10, 
            lw=2, arrowstyle="-|>", color="black")
ax.add_artist(a)
b = Arrow3D([x[3],x[3]], [y[3],y[3]], 
            [z[3]-1,z[3]+1], mutation_scale=2, 
            lw=1, arrowstyle="|-|", color="black")
ax.add_artist(b)
c = Arrow3D([x[3]+1,x[3]-1], [y[3],y[3]], 
            [z[3],z[3]], mutation_scale=2, 
            lw=1, arrowstyle="|-|", color="black")
ax.add_artist(c)
d = Arrow3D([x[3],x[3]], [y[3]+1,y[3]-1], 
            [z[3],z[3]], mutation_scale=2, 
            lw=1, arrowstyle="|-|", color="black")
ax.add_artist(d)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Altitude')

plt.show()