import cv2, sys
import numpy as np

src = cv2.imread('data2/rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    sys.exit('Image load failed')

# 사용자 커널(=필터)을 생성해서 blur
kernel = np.ones((3,3), dtype=np.float32)/9
dst = cv2.filter2D(src, -1, kernel)

# blur kernel을 사용해서
dst2 = cv2.blur(src, (3,3))

cv2.imshow('src',src)
cv2.imshow('dst',dst)
cv2.imshow('dst2',dst2)
cv2.waitKey()
cv2.destroyAllWindows()