
"""
This a sample Hand-Finger's Landmark Detection
 with the help of Python Programming.

 Raise your hand in front of your camera (front)
  to see the landmarks, expected vision, desired movements of virtual finger points as pointer

### Hi, I'm Mazharul Islam Bhuiyan
I have to use the following:
# opencv(Open Source Computer Vision Library),
# mediapipeline(offers cross-platform,
# customizable ML solutions for live and streaming media),
# pyautogui (Python packagethe to simulate mouse cursor moves and clicks as well as keyboard button presses.),
# Protobuf (Protocol Buffers): free and open-source cross-platform data format used to serialize structured data, developing programs to communicate with each other over a network or for storing data.

"""

import cv2
import mediapipe as mp

cam_capture = cv2.VideoCapture(0)
pointer_hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
while True:
    _, vid_frame = cam_capture.read()
    vid_frame = cv2.flip(vid_frame, 1)  # flipping Video Capture for front camera as it behaves like mirror reflection
    rgb_Frame = cv2.cvtColor(vid_frame, cv2.COLOR_BGR2RGB)
    result = pointer_hand_detector.process(rgb_Frame)
    pointer_hands = result.multi_hand_landmarks
    # print(pointer_hands)

    if pointer_hands:
        for hand_point in pointer_hands:
            drawing_utils.draw_landmarks(vid_frame, hand_point)
    cv2.imshow('Mouse Virtual_Pointer', vid_frame)
    cv2.waitKey(1)