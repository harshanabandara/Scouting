#%%
from utils import load_head_hand_eye_data
from project_hand_eye_to_pv import get_eye_gaze_point
import cv2
import numpy as np
# %%
timestamps, head_transs, left_hand_transs, left_hand_transs_available,\
            right_hand_transs, right_hand_transs_available, gaze_data, gaze_available = load_head_hand_eye_data('2022-11-11-122352_head_hand_eye.csv')
# %%
data = np.loadtxt('2022-11-11-122352_head_hand_eye.csv', delimiter=',')
# %%
print(gaze_data.shape)
# %%
xy, _ = cv2.projectPoints(point.reshape((1, 3)), rvec, tvec, K, None)
# %%
print(gaze_data[0])
# %%
print(right_hand_transs[0])
# %%
print(right_hand_transs_available[0])
# %%
print(gaze_data[0].shape)
# %%
print(left_hand_transs[0].shape)
# %%
