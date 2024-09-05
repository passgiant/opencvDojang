# inRange 함수를 잘 설정하려면 trackBar 기능이 필요하다.

import sys
import cv2

# 트랙바 콜백 함수 생성
def on_trackbar(pos):
    hmin = cv2.getTrackbarPos('H_min', 'Trackbar')
    hmax = cv2.getTrackbarPos('H_max', 'Trackbar')
    
    #red 검출
    #dst = cv2.inRange(src_hsv, (hmin,100,0), (hmax,255,255))
    mask_red1 = cv2.inRange(src_hsv,(0,100,0),(10,255,255))
    mask_red2 = cv2.inRange(src_hsv,(160,100,0),(180,255,255))
    mask_red = cv2.bitwise_or(mask_red1,mask_red2)
    
    #yellow 검출
    mask_yellow = cv2.inRange(src_hsv,(15,100,0),(35,255,255))
    
    #green 검출
    mask_green = cv2.inRange(src_hsv,(50,100,0),(75,255,255))
    
    red_pixels = cv2.countNonZero(mask_red)
    yellow_pixels = cv2.countNonZero(mask_yellow)
    green_pixels = cv2.countNonZero(mask_green)
    
    color_pixels = {
        'red': red_pixels,
        'yellow': yellow_pixels,
        'green': green_pixels
    }
    
    max_color = max(color_pixels, key=color_pixels.get)
    
    print(max_color)
    
    # print('r_count:', red_pixels)
    # print('y_count:', yellow_pixels)
    # print('g_count:', green_pixels)
    
    # if red_pixels > yellow_pixels and red_pixels > green_pixels:
    #     print('red')
    # elif yellow_pixels > red_pixels and yellow_pixels > green_pixels:
    #     print('yellow')
    # elif green_pixels > red_pixels and green_pixels > yellow_pixels:
    #     print('green')
    
    cv2.imshow('Trackbar', mask_green)

#fileName = 'data2/red.jpg'
fileName = 'data2/green.jpg'
#fileName = 'data2/yellow.jpg'

src = cv2.imread(fileName)

if src is None:
    sys.exit('Image Load failed!')
    
# 색상의 범위를 잘 지정하려면 bgr -> hsv
src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

# 창에 트랙바를 넣기 위해서는 창을 먼저 생성
cv2.namedWindow('Trackbar')
cv2.imshow('Trackbar', src_hsv)

# 트랙바 생성: 'H_min' 트랙바의 이름, 범위-~255, 
# on_trackbar: 트랙바를 움직일 때 호출되는 함수(콜백함수)
cv2.createTrackbar('H_min', 'Trackbar', 0, 180, on_trackbar)
cv2.createTrackbar('H_max', 'Trackbar', 0, 180, on_trackbar)
on_trackbar(0)

cv2.waitKey()
cv2.destroyAllWindows()