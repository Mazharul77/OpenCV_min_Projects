"""
@ Mazharul Islam Bhuiyan
 Eye Controlling Mouse system: Now moving eyeball, tip eyelid as like as virtual mouse

"""
import cv2
import mediapipe as mp
import pyautogui
device_camera = cv2.VideoCapture(0)
face_detect = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
device_screen_height, device_screen_height = pyautogui.size()
while True:
    interface_, device_video_frame = device_camera.read()
    device_video_frame = cv2.flip(device_video_frame, 1)
    rgbColor_frame = cv2.cvtColor(device_video_frame, cv2.COLOR_BGR2RGB)
    face_result = face_detect.process(rgbColor_frame)
    face_landmark_points = face_result.multi_face_landmarks

    height_vid_frame, width_vid_frame, _ = device_video_frame.shape

    # print("No. Of Landmarks in Eyes: ")
    if face_landmark_points:
        landmark_points = face_landmark_points[0].landmark
        # detection of Eye-Landmark(4 points within eyelids)

        for each_pupil_index, each_lpoint in enumerate(landmark_points[474:478]):
            # print(len(landmark_points)) # Calculating Total Landmark points
            x_axis_point = int(each_lpoint.x * width_vid_frame)
            y_axis_point = int(each_lpoint.y * height_vid_frame)
            # print(x_axis_point, y_axis_point)

            # let draw circle shaped eye-landmarks points
            # within the video frame as RGB color detected
            cv2.circle(device_video_frame, (x_axis_point, y_axis_point), 3, (0, 255, 0))

            if each_pupil_index == 1:
                scrn_x = 1.7 * (width_vid_frame/width_vid_frame * x_axis_point)
                scrn_y = 1.4 * (device_screen_height/height_vid_frame * y_axis_point)
                pyautogui.moveTo(scrn_x, scrn_y)

        left_eye_lids = [landmark_points[159], landmark_points[145]]
        for lefte_eye_landmark in left_eye_lids:
           left_eye_x = int(lefte_eye_landmark.x * width_vid_frame)
           left_eye_y = int(lefte_eye_landmark.y * height_vid_frame)
           cv2.circle(device_video_frame, (left_eye_x, left_eye_y), 3, (255, 0, 255))

        # print(left_eye_lids[1].y - left_eye_lids[0].y)
        if (left_eye_lids[1].y - left_eye_lids[0].y) < 0.005:
            pyautogui.click()  # click() will be happened
            print("Clicked !")
            pyautogui.sleep(1.5)


    cv2.imshow('Virtual Eye Controlled Mouse', device_video_frame)
    cv2.waitKey(1)

