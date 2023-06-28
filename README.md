### Following files require before running the script.
- 2022-11-11-122352_head_hand_eye.csv
- 2022-11-11-122352_pv.txt
- Depth Long Throw_extrinsics.txt
- Depth Long Throw_lut.bin
- Depth Long Throw_rig2world.txt
- Depth Long Throw.tar
- PV.tar
#### head_hand_eye.csv
- timestamp : 0
- head_transs : [1:16]
- head_trainss_available: 17
- left_hand_transs : 26x3 
- right_hand_transs : 26x3
- gaze_data : 9
#### pv.txt
### Instructions
- run the process_all.py by `python3 process_all --recording_path . --project_hand_eye`
- to generate the 3D map, run `python3 tsdf-integration.py --pinhole_path pinhole_projection`

### cv2.projectPoints(objectPoints, rvec, tvec, cameraMatrix, distCoeffs[, imagePoints[, jacobian[, aspectRatio]]]	) -> 	imagePoints, jacobian
Projects 3D points to an image plane.

#### Parameters
- objectPoints	Array of object points expressed wrt. the world coordinate frame. A 3xN/Nx3 1-channel or 1xN/Nx1 3-channel (or vector<Point3f> ), where N is the number of points in the view.
- rvec	The rotation vector (Rodrigues) that, together with tvec, performs a change of basis from world to camera coordinate system, see calibrateCamera for details.
- tvec	The translation vector, see parameter description above.
- cameraMatrix	Camera intrinsic matrix A=⎡⎣⎢fx000fy0cxcy1⎤⎦⎥ .
- distCoeffs	Input vector of distortion coefficients (k1,k2,p1,p2[,k3[,k4,k5,k6[,s1,s2,s3,s4[,τx,τy]]]]) of 4, 5, 8, 12 or 14 elements . If the vector is empty, the zero distortion coefficients are assumed.
- imagePoints	Output array of image points, 1xN/Nx1 2-channel, or vector<Point2f> .
- jacobian	Optional output 2Nx(10+<numDistCoeffs>) jacobian matrix of derivatives of image points with respect to components of the rotation vector, translation vector, focal lengths, coordinates of the principal point and the distortion coefficients. In the old interface different components of the jacobian are returned via different output parameters.
- aspectRatio	Optional "fixed aspect ratio" parameter. If the parameter is not 0, the function assumes that the aspect ratio ( fx/fy) is fixed and correspondingly adjusts the jacobian matrix.

The function computes the 2D projections of 3D points to the image plane, given intrinsic and extrinsic camera parameters. Optionally, the function computes Jacobians -matrices of partial derivatives of image points coordinates (as functions of all the input parameters) with respect to the particular parameters, intrinsic and/or extrinsic. The Jacobians are used during the global optimization in calibrateCamera, solvePnP, and stereoCalibrate. The function itself can also be used to compute a re-projection error, given the current intrinsic and extrinsic parameters.

Note
    By setting rvec = tvec = [0,0,0], or by setting cameraMatrix to a 3x3 identity matrix, or by passing zero distortion coefficients, one can get various useful partial cases of the function. This means, one can compute the distorted coordinates for a sparse set of points or apply a perspective transformation (and also compute the derivatives) in the ideal zero-distortion setup. 