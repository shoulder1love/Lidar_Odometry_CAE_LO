import numpy as np
import matplotlib.pyplot as plt


# Read the binary file
file_path = "kitti000081.bin"
file_path = "data2/000081.bin"
data = np.fromfile(file_path, dtype=np.float32)
print(data.shape)

# Reshape the data to extract x, y, z, and r values
data = data.reshape(-1, 4)
print(data)
x = data[:, 0]
y = data[:, 1]
z = data[:, 2]
r = data[:, 3]

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# Scatter plot the points with color
ax.scatter(x, y, z, c=r, cmap="jet")

# Set labels and title
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Point Cloud Visualization")

# Show the plot
plt.show()