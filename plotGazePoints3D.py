
from utils import load_head_hand_eye_data
from project_hand_eye_to_pv import get_eye_gaze_point
# import cv2
import numpy as np
from matplotlib import pyplot as plt
timestamps, head_transs, left_hand_transs, left_hand_transs_available,\
            right_hand_transs, right_hand_transs_available, gaze_data, gaze_available = load_head_hand_eye_data('2022-11-11-122352_head_hand_eye.csv')

data = np.loadtxt('2022-11-11-122352_head_hand_eye.csv', delimiter=',')

print(gaze_data.shape)
nFrames = len(gaze_data)
fig = plt.figure(figsize=[10,10])
ax = fig.add_subplot(projection='3d')
x,y,z = [0 for _ in range(nFrames)],[0 for _ in range(nFrames)],[0 for _ in range(nFrames)]
for i in range(nFrames):
    if gaze_available[i]:
        x[i],y[i],z[i]= get_eye_gaze_point(gaze_data[i])
        x[i],y[i],z[i]= gaze_data[i][:3]
ax.scatter(x,y,z,c=timestamps)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Gaze Coordinates in 3D')
ax.set_zlabel('z')

plt.savefig("3d plot of gaze coordinates.png")
plt.show()
plt.close()
# xy, _ = cv2.projectPoints(point.reshape((1, 3)), rvec, tvec, K, None)

# print(gaze_data[0])

# print(right_hand_transs[0])

# print(right_hand_transs_available[0])

# print(gaze_data[0].shape)

# print(left_hand_transs[0].shape)

