import numpy as np
import open3d as o3d
import os

input_path = '/Users/yeelu/desktop/omer_gt_transform/'

output_path = '/Users/yeelu/desktop/omer_gt_pc_npy/'

ply_list = os.listdir(input_path)

for ply in ply_list:

    input = os.path.join(input_path, ply)

    # Load saved point cloud and visualize it'
    pcd_load = o3d.io.read_point_cloud(input)

    # convert Open3D.o3d.geometry.PointCloud to numpy array
    xyz_load = np.asarray(pcd_load.points)

    file_name = "{0}npy".format(ply[:-3])
    output = os.path.join(output_path, file_name)
    np.save(output, xyz_load)

# pcd = o3d.geometry.PointCloud()
# pcd.points = o3d.utility.Vector3dVector(B)
# o3d.io.write_point_cloud("/content/gdrive/My Drive/Colab Notebooks/point_cloud/points2surf/03_meshes/mesh/1e7c8833d231178fdcddd0cba5e9fbec.ply", pcd)