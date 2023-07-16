import os

import struct
import numpy as np
import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D

def read_bin_file(filename):
    with open(filename, 'rb') as f:
        data = f.read()


    num_points = len(data) // struct.calcsize('fffBBB')
    point_cloud = np.zeros((num_points, 4), dtype=np.float32)
    colors = np.zeros((num_points, 3), dtype=np.uint8)
    # # Reshape the array to have five columns
    # reshaped_array = original_array.reshape(-1, 6)

    # # Extract the first three elements from each row
    # extracted_array = reshaped_array[:, :3].flatten()

    for i in range(num_points):
        offset = i * struct.calcsize('fffBBB')
        x, y, z, r, g, b = struct.unpack('fffBBB', data[offset:offset + struct.calcsize('fffBBB')])
        point_cloud[i] = [x, y, z, r]
        colors[i] = [r, g, b]

    return point_cloud, colors

# Define the source folder and target folder paths
source_folder = "data1"
target_folder = "data_after"

# Find all .txt files in the source folder
txt_files = [file for file in os.listdir(source_folder) if file.endswith(".bin")]

# Iterate through each .txt file
for txt_file in txt_files:
    # Get the file path for the current .txt file
    file_path = os.path.join(source_folder, txt_file)

    # Open the file for reading
    point_cloud, colors = read_bin_file(file_path)



    # Create the target file path
    target_file_path = os.path.join(target_folder, txt_file)
    point_cloud.tofile(target_file_path)



    print(f"File '{txt_file}' has been processed and saved to the target folder.")