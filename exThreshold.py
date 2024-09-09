import cv2, sys
import matplotlib.pyplot as plt
import myLib

src = cv2.imread('data2/apple_th.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    sys.exit('Image load failed')

myLib.hist_gray(src)

_, src_th = cv2.threshold(src, 170, 255, cv2.THRESH_BINARY)
cv2.imshow('src', src)
cv2.imshow('src_th', src_th)
cv2.waitKey()
cv2.destroyAllWindows()