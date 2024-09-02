import cv2
import sys
from matplotlib import pyplot as plt

fileName = 'data/cat.jpg'

img = cv2.imread(fileName)

if img is None:
    sys.exit('Image load is failed')
    
# opencv 모듈은 이미지를 읽어올 때 컬러 스페이스의 순서
# B_G_R

# 컬러 스페이스(채널 순서)를 바꿔주는 함수
imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# matplotlib은 R, G, B로 사용

plt.imshow(imgRGB)
plt.axis('off')
plt.show()