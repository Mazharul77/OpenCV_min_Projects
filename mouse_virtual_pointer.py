
""""
This a sample mouse pointer (as circle pointer) which is a virtual mouse
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
import pyautogui
cam_capture = cv2.VideoCapture(0)
pointer_hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
device_screen_width, device_screen_height = pyautogui.size()
scrn_y = 0
while True:
    _, vid_frame = cam_capture.read()
    vid_frame = cv2.flip(vid_frame, 1)  # flipping Video Capture for front camera as it behaves like mirror reflection
    rgb_Frame = cv2.cvtColor(vid_frame, cv2.COLOR_BGR2RGB)
    vid_frame_height, vid_frame_width, _ = vid_frame.shape
    result = pointer_hand_detector.process(rgb_Frame)
    pointer_hands = result.multi_hand_landmarks
    # print(pointer_hands)

    if pointer_hands:
        for hand_point in pointer_hands:
            drawing_utils.draw_landmarks(vid_frame, hand_point)
            hand_landmarks = hand_point.landmark
            for id, landmark_ in enumerate(hand_landmarks):
                x_axis = int(landmark_.x * vid_frame_width)
                y_axis = int(landmark_.y * vid_frame_height)
                if id == 8:
                    cv2.circle(img=vid_frame, center=(x_axis, y_axis), radius=10, color=(0, 255, 0))
                    scrn_x = device_screen_width / vid_frame_width * x_axis
                    scrn_y = device_screen_height / vid_frame_height * y_axis
                    pyautogui.moveTo(scrn_x, scrn_y)
                    # print(scrn_x, scrn_y)

                if id == 4:
                    cv2.circle(img=vid_frame, center=(x_axis, y_axis), radius=10, color=(0, 255, 0))
                    thumbnail_x = device_screen_width / vid_frame_width * x_axis
                    thumbnail_y = device_screen_height / vid_frame_height * y_axis
                    print('Not_Clicked: Distacne_2_finger', abs(scrn_y-thumbnail_y))
                    if abs(scrn_y-thumbnail_y) < 20:
                        # print('Click Ok', abs(scrn_y - thumbnail_y))
                        pyautogui.click()
                        pyautogui.sleep(1)
    cv2.imshow('Mouse Virtual_Pointer', vid_frame)
    cv2.waitKey(1)