import cv2, sys
import numpy as np

# 화살표를 누르면 원이 이동되는 어플

width, height = 512, 512

#초기의 원의 좌표와 반지름
x, y, r = 256, 256, 50

direction = 0

#main
while True:
    #빈 캔버스 생성
    img = np.zeros((width, height, 3), np.uint8)+255
    cv2.circle(img, (x,y), r, (255,255,0), -1)
    cv2.imshow('img', img)
    
    # 기본 waitKey + Extension 키 입력까지 받아들임
    key = cv2.waitKeyEx(30) #delay 30
    #종료 조건
    if key == 27: #ESC
        break
    #right key
    elif key == 0x270000:
        direction = 0
        x += 10
    #down key
    elif key == 0x280000:
        direction = 1
        y += 10
    #left key
    elif key == 0x250000:
        direction = 2
        x -= 10
    #up key
    elif key == 0x260000:
        direciton = 3
        y -= 10
    
    if x < r:
        x = r
        direction = 0
    if x > width - r:
        x = width - r
        direction = 2
    if y < r:
        y = r
        direction = 1
    if y > height - r:
        y = height - r
        direction = 3

cv2.destroyAllWindows()