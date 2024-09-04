import cv2
import time
from datetime import datetime
import os

cap = cv2.VideoCapture(0)

# print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # 640
# print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # 480

fourcc = cv2.VideoWriter_fourcc(*'XVID')
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 30)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

video_duration = 60
total_duration = 10 * 60
num_videos = total_duration // video_duration

recording = True
video_count = 0
start_time = time.time()

while recording:

    base_folder = 'bb'
    folder_name = os.path.join(base_folder, datetime.now().strftime('%Y%m%d_%H%M'))

    if not os.path.exists(base_folder):
        os.makedirs(base_folder)

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    current_time = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = os.path.join(folder_name, f'{current_time}.avi')
    out = cv2.VideoWriter(filename, fourcc, fps, (width, height))

    video_start_time = time.time()
    while time.time() - video_start_time < video_duration:
        ret, frame = cap.read()
        if ret:
            out.write(frame)
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                recording = False
                break
        else:
            break
    
    out.release()
    video_count += 1

    if video_count >= num_videos:
        recording = False

if cap.isOpened():
    cap.release()
cv2.destroyAllWindows()