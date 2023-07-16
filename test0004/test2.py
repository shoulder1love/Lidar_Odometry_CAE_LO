import numpy as np
import mayavi.mlab as mlab

# Create a trojectory
theta = np.linspace(0, 2 * np.pi, 100)
x = 2 * np.sin(3 * theta)
y = np.cos(4 * theta)
z = np.sin(2 * theta)

# Create a 3D plot
mlab.figure(bgcolor=(1, 1, 1))
mlab.plot3d(x, y, z, color=(0, 1, 0), tube_radius=0.025)

# Set labels and title
mlab.xlabel('X')
mlab.ylabel('Y')
mlab.zlabel('Z')
mlab.title('Trojectory')

# Show the plot
mlab.show()