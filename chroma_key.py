import sys
import numpy as np
import cv2

fileName1 = 'data2/woman.mp4'
fileName2 = 'data2/raining.mp4'

cap1 = cv2.VideoCapture(fileName1)
cap2 = cv2.VideoCapture(fileName2)

if not cap1.isOpened():
    sys.exit('video1 open failed')
    
if not cap2.isOpened():
    print('video2 open failed')
    sys.exit()
    
fps1 = int(cap1.get(cv2.CAP_PROP_FPS))
fps2 = int(cap2.get(cv2.CAP_PROP_FPS))

# 동영상의 총 프레임
frameCount1 = int(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frameCount2 = int(cap2.get(cv2.CAP_PROP_FRAME_COUNT))

# print(fps1)
# print(fps2)

# print(frameCount1)
# print(frameCount2)

# 초당 몇 프레임: 1번 동영상 기준
delay = int(1000/fps1)

# 합성 여부 설정 플래그
do_composite = False

while True:
    ret1, frame1 = cap1.read()
    if not ret1:
        break
    
    if do_composite:
        ret2, frame2 = cap2.read()
        if not ret2:
            break
    
        # hsv 색공간에서 영역을 검출해서 합성
        hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
        # h: 50~70, s: 150~255, v: 0~255
        mask = cv2.inRange(hsv,(50,150,0),(70,255,255))
        cv2.copyTo(frame2, mask, frame1)
    
    # 결과 확인
    cv2.imshow('frame', frame1)
    key = cv2.waitKey(delay)
    # 스페이스 바를 눌렀을 때 do_composite를 반전
    if key == ord(' '):
        do_composite = not do_composite
    elif key == 27:
        break
    
cap1.release()
cap2.release()
cv2.destroyAllWindows()