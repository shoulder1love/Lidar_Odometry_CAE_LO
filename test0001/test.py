
import numpy as np
import mayavi.mlab

'''
calib=np.loadtxt("calib.txt")
print(calib)
Tr=np.array(calib[4,:].reshape(3,4),dtype=np.float32)
print(Tr)
'''

PC = np.load("PC.npy")
PC1 =    np.load("PC1.npy")
PC2 =    np.load("PC2.npy")
VoxelPC = np.load("VoxelPC.npy")
SingleColor0 =     np.load("SingleColor0.npy")
SingleColor1 =    np.load("SingleColor1.npy")
color1=     np.load("color1.npy")
color2 =    np.load("color2.npy")

fig = mayavi.mlab.figure(bgcolor=(0, 0, 0), size=(1640, 1500))

node_PC = mayavi.mlab.points3d(PC[:,0], PC[:,1], PC[:,2],
                        mode="point",figure=fig)
node_PC.mlab_source.dataset.point_data.scalars = SingleColor0

node_VoxelPC=mayavi.mlab.points3d(VoxelPC[:,0], VoxelPC[:,1], VoxelPC[:,2],
                        mode="point",figure=fig)
node_VoxelPC.glyph.scale_mode = 'scale_by_vector'
node_VoxelPC.mlab_source.dataset.point_data.scalars = SingleColor1

node_PC1=mayavi.mlab.points3d(PC1[:,0], PC1[:,1], PC1[:,2],
                        scale_factor=0.02, figure=fig)
node_PC1.glyph.scale_mode = 'scale_by_vector'
node_PC1.mlab_source.dataset.point_data.scalars = color1

node_PC2=mayavi.mlab.points3d(PC2[:,0], PC2[:,1], PC2[:,2],
                        scale_factor=0.1, figure=fig)
node_PC2.glyph.scale_mode = 'scale_by_vector'
node_PC2.mlab_source.dataset.point_data.scalars = color2

mayavi.mlab.show()