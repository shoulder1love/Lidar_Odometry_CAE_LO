'''
import numpy as np

# Create a NumPy array with more than 20 integers
original_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                           11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                           21, 22, 23, 24, 25])

# Reshape the array to have five columns
reshaped_array = original_array.reshape(-1, 5)

# Extract the first three elements from each row
extracted_array = reshaped_array[:, :3].flatten()

# Print the extracted elements
print("Extracted Elements:")
print(extracted_array)

'''
import struct
import numpy as np
import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D

def read_bin_file(filename):
    with open(filename, 'rb') as f:
        data = f.read()
    # print(data.shape)
    print(type(data))

    num_points = len(data) // struct.calcsize('fffBBB')
    point_cloud = np.zeros((num_points, 3), dtype=np.float32)
    colors = np.zeros((num_points, 3), dtype=np.uint8)
    # # Reshape the array to have five columns
    # reshaped_array = original_array.reshape(-1, 6)

    # # Extract the first three elements from each row
    # extracted_array = reshaped_array[:, :3].flatten()

    for i in range(num_points):
        offset = i * struct.calcsize('fffBBB')
        x, y, z, r, g, b = struct.unpack('fffBBB', data[offset:offset + struct.calcsize('fffBBB')])
        point_cloud[i] = [x, y, z]
        print(point_cloud[i] )
        colors[i] = [r, g, b]

    return point_cloud, colors

def visualize_point_cloud(point_cloud, colors):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(point_cloud[:, 0], point_cloud[:, 1], point_cloud[:, 2], c=colors/255.0)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()

if __name__ == '__main__':
    filename = 'kitti000081.bin'
    filename = 'data1/000081.bin'
    point_cloud, colors = read_bin_file(filename)
    visualize_point_cloud(point_cloud, colors)