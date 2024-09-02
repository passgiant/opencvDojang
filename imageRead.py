# 파일에서 이미지를 읽어서 출력

import cv2
import sys

fileName = 'data/cat.jpg'

img = cv2.imread(fileName)
print(img.shape)
if img is None:
    print('Image load fail')
    sys.exit()
    
cv2.namedWindow('img')
cv2.imshow('img', img)

cv2.imwrite('cat1.png', img, [cv2.IMWRITE_JPEG_QUALITY, 85])
cv2.imwrite('cat2.png', img, [cv2.IMWRITE_JPEG_QUALITY, 95])

while True:
    if cv2.waitKey() == ord('q'):
        cv2.destroyWindow('img')
        #cv2.destroyAllWindows()
        break