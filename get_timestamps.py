import numpy as np
from utils import HandJointIndex
def getFrameData(csv_path):
    '''
        a function to get the time stamps of each image.
        timestamp of image | timestamp of eye data | image path | wheather the image has a switch or a human
    '''
    joint_count = HandJointIndex.Count.value

    data = np.loadtxt(csv_path, delimiter=',')

    n_frames = len(data)
    timestamps = np.zeros(n_frames)
    head_transs = np.zeros((n_frames, 3))

    left_hand_transs = np.zeros((n_frames, joint_count, 3))
    left_hand_transs_available = np.ones(n_frames, dtype=bool)
    right_hand_transs = np.zeros((n_frames, joint_count, 3))
    right_hand_transs_available = np.ones(n_frames, dtype=bool)

    # origin (vector, homog) + direction (vector, homog) + distance (scalar)
    gaze_data = np.zeros((n_frames, 9))
    gaze_available = np.ones(n_frames, dtype=bool)

    for i_frame, frame in enumerate(data):
        timestamps[i_frame] = frame[0]
        # head
        head_transs[i_frame, :] = frame[1:17].reshape((4, 4))[:3, 3]
        # left hand
        left_hand_transs_available[i_frame] = (frame[17] == 1)
        left_start_id = 18
        for i_j in range(joint_count):
            j_start_id = left_start_id + 16 * i_j
            j_trans = frame[j_start_id:j_start_id + 16].reshape((4, 4))[:3, 3]
            left_hand_transs[i_frame, i_j, :] = j_trans
        # right hand
        right_hand_transs_available[i_frame] = (
            frame[left_start_id + joint_count * 4 * 4] == 1)
        right_start_id = left_start_id + joint_count * 4 * 4 + 1
        for i_j in range(joint_count):
            j_start_id = right_start_id + 16 * i_j
            j_trans = frame[j_start_id:j_start_id + 16].reshape((4, 4))[:3, 3]
            right_hand_transs[i_frame, i_j, :] = j_trans

        assert(j_start_id + 16 == 851)
        gaze_available[i_frame] = (frame[851] == 1)
        gaze_data[i_frame, :4] = frame[852:856]
        gaze_data[i_frame, 4:8] = frame[856:860]
        gaze_data[i_frame, 8] = frame[860]

    return (timestamps, head_transs, left_hand_transs, left_hand_transs_available,
            right_hand_transs, right_hand_transs_available, gaze_data, gaze_available)

def get_eye_gaze_point(gaze_data):
    origin_homog = gaze_data[:4]
    direction_homog = gaze_data[4:8]
    direction_homog = direction_homog / np.linalg.norm(direction_homog)
    # if no distance was recorded, set 1m by default
    dist = gaze_data[8] if gaze_data[8] > 0.0 else 1.0
    point = origin_homog + direction_homog * dist
    print(point)
    return point[:3]
if __name__ == "__main__":
    timestamps,_,_,_,_,_,gaze_data,gaze_available = getFrameData("2022-11-11-122352_head_hand_eye.csv")
    # print("Timestamps")
    # print(timestamps)
    # print("Gaze data")
    # print(gaze_data)

    for i in range(len(timestamps)):
        # print(f'{timestamps[i]} {gaze_data[i]}')
        get_eye_gaze_point(gaze_data[i])