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