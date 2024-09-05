import sys
import cv2

def on_trackbar(pos):
    hmin1 = cv2.getTrackbarPos('H_min', 'red')
    hmax1 = cv2.getTrackbarPos('H_max', 'red')
    
    hmin2 = cv2.getTrackbarPos('H_min', 'yellow')
    hmax2 = cv2.getTrackbarPos('H_max', 'yellow')
    
    hmin3 = cv2.getTrackbarPos('H_min', 'green')
    hmax3 = cv2.getTrackbarPos('H_max', 'green')

    dst1 = cv2.inRange(img1_hsv, (hmin1,100,100), (hmax1,255,255))
    dst2 = cv2.inRange(img2_hsv, (hmin2,100,100), (hmax2,255,255))
    dst3 = cv2.inRange(img3_hsv, (hmin3,100,100), (hmax3,255,255))
    
    cv2.imshow('red', dst1)
    cv2.imshow('yellow', dst2)
    cv2.imshow('green', dst3)

path1 = 'data2/red.jpg'
path2 = 'data2/yellow.jpg'
path3 = 'data2/green.jpg'

img1 = cv2.imread(path1)
img2 = cv2.imread(path2)
img3 = cv2.imread(path3)

if img1 is None:
    sys.exit('Image1 Load failed!')
if img2 is None:
    sys.exit('Image2 Load failed!')
if img3 is None:
    sys.exit('Image3 Load failed!')

img1_hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
img2_hsv = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
img3_hsv = cv2.cvtColor(img3, cv2.COLOR_BGR2HSV)

# namedWindow는 어떤 함수?
cv2.namedWindow('red')
cv2.namedWindow('yellow')
cv2.namedWindow('green')

cv2.createTrackbar('H_min', 'red', 0, 10, on_trackbar)
cv2.createTrackbar('H_max', 'red', 170, 180, on_trackbar)

cv2.createTrackbar('H_min', 'yellow', 20, 30, on_trackbar)
cv2.createTrackbar('H_max', 'yellow', 20, 30, on_trackbar)

cv2.createTrackbar('H_min', 'green', 35, 85, on_trackbar)
cv2.createTrackbar('H_max', 'green', 35, 85, on_trackbar)

cv2.waitKey()
cv2.destroyAllWindows()