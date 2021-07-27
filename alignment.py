# examples/Python/Basic/icp_registration.py

import open3d as o3d
import numpy as np
import copy
# from o3d.geometry import estimate_normals, KDTreeSearchParamHybrid

def draw_registration_result(source, target, transformation):
    source_temp = copy.deepcopy(source)
    target_temp = copy.deepcopy(target)
    source_temp.paint_uniform_color([1, 0.706, 0])
    target_temp.paint_uniform_color([0, 0.651, 0.929])
    source_temp.transform(transformation)
    o3d.visualization.draw_geometries([source_temp, target_temp])


if __name__ == "__main__":
    source = o3d.io.read_point_cloud("1b2a8980c17fdd97c897e89b561760b1_4.ply")
    target = o3d.io.read_point_cloud("1b2a8980c17fdd97c897e89b561760b1_5.ply")
    threshold = 0.02
    trans_init = np.asarray([[0.862, 0.011, -0.507, 0.5],
                             [-0.139, 0.967, -0.215, 0.7],
                             [0.487, 0.255, 0.835, -1.4], [0.0, 0.0, 0.0, 1.0]])
    draw_registration_result(source, target, trans_init)
    print("Initial alignment")
    evaluation = o3d.pipelines.registration.evaluate_registration(source, target,
                                                        threshold, trans_init)
    print(evaluation)

    print("Apply point-to-point ICP")
    reg_p2p = o3d.pipelines.registration.registration_icp(
        source, target, threshold, trans_init,
        o3d.pipelines.registration.TransformationEstimationPointToPoint())
    print(reg_p2p)
    print("Transformation is:")
    print(reg_p2p.transformation)
    print("")
    draw_registration_result(source, target, reg_p2p.transformation)

    print("Apply point-to-plane ICP")

    o3d.geometry.PointCloud.estimate_normals(source, search_param = o3d.geometry.KDTreeSearchParamHybrid( radius = 0.1, max_nn = 30))
    o3d.geometry.PointCloud.estimate_normals(target, search_param = o3d.geometry.KDTreeSearchParamHybrid( radius = 0.1, max_nn = 30))
    reg_p2l = o3d.pipelines.registration.registration_icp(
        source, target, threshold, trans_init, 
        o3d.pipelines.registration.TransformationEstimationPointToPlane())
    # reg_p2l = o3d.pipelines.registration.registration_icp(
    #     source, target, threshold, trans_init,
    #     o3d.pipelines.registration.TransformationEstimationPointToPlane())
    print(reg_p2l)
    print("Transformation is:")
    print(reg_p2l.transformation)
    print("")
    draw_registration_result(source, target, reg_p2l.transformation)