import numpy as np
from matplotlib import pyplot as plt

with open('pinhole_projection/trajectory.xyz') as f:
    lines = f.readlines()
nPts = len(lines)
x,y,z = np.zeros((3,nPts))
for i_line, line in enumerate(lines):
    x[i_line],y[i_line],z[i_line] = list(map(float,line.strip().split()))

fig = plt.figure(figsize=[10,10])
ax = fig.add_subplot(projection='3d')
ax.scatter(x,y,z)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Trajectory Coordinates in 3D')
ax.set_zlabel('z')

plt.savefig("3d plot of trajectory coordinates.png")
plt.show()
plt.close()