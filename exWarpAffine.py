import cv2, sys
import numpy as np
import math

def translate(src, x_move, y_move):
    #이미지의 이동 변환
    aff = np.array([[1,0,x_move],[0,1,y_move]], dtype=np.float32)
    dst = cv2.warpAffine(src, aff, (0,0)) # dsize: w+x_move, h+y_move, width가 먼저 오는 게 맞다 함, by 퍼플렉시티
    return dst

def shear(src, x_shear=0, y_shear=0):
    h, w = src.shape[:2]
    if x_shear>0 and y_shear==0:
        aff = np.array([[1, x_shear, 0],[0, 1, 0]], dtype=np.float32)
        dst = cv2.warpAffine(src, aff, (w + int(h * x_shear), h))
    elif x_shear==0 and y_shear>0:
        aff = np.array([[1, 0, 0],[y_shear, 1, 0]], dtype=np.float32)
        dst = cv2.warpAffine(src, aff, (w, h + int(w * y_shear)))
    return dst

def scale(src, x_scale, y_scale):
    h, w = src.shape[:2]
    aff = np.array([[x_scale, 0, 0],[0, y_scale, 0]], dtype=np.float32)
    dst = cv2.warpAffine(src, aff, (0,0))
    return dst

def rotate(src, rad):
    aff = np.array([[np.cos(rad), np.sin(rad), 0], [-np.sin(rad), np.cos(rad), 0]], dtype=np.float32)
    dst = cv2.warpAffine(src, aff, (0, 0))
    return dst

def rotate2(src, angle):
    h, w = src.shape[:2]
    centerPt = (w/2, h/2)
    # getRotationMatrix2D가 알아서 변환행렬 만들어줌
    aff = cv2.getRotationMatrix2D(centerPt, angle, 1)
    dst = cv2.warpAffine(src, aff, (w, h))
    return dst

#src = cv2.imread('data/lena.bmp')
src = cv2.imread('data2/rose.bmp')

if src is None:
    sys.exit('Image load failed')

#dst = shear(src, 0.5, 0)
#dst = scale(src, 0.5, 0.5)

# 512x512 -> 1024x1024
#dst = cv2.resize(src, (1024,1024))

#비율로 설정
#dst = cv2.resize(src, (0,0), fx=1.5, fy=1.5)

# 여기서부터 lose
# dst = cv2.resize(src, (0,0), fx=3, fy=3)
# dst1 = cv2.resize(src, (0,0), fx=3, fy=3, interpolation=cv2.INTER_CUBIC)
# dst2 = cv2.resize(src, (0,0), fx=3, fy=3, interpolation=cv2.INTER_NEAREST)
# dst3 = cv2.resize(src, (0,0), fx=3, fy=3, interpolation=cv2.INTER_LANCZOS4)

#각도를 라디안으로 변환하는 공식
# angle = 20
# rad = angle*math.pi/180
# dst = rotate(src, rad)

dst = rotate2(src, 180)

#cv2.imshow('src',src)
cv2.imshow('dst',dst)
# cv2.imshow('dst1', dst1)
# cv2.imshow('dst2', dst2)
# cv2.imshow('dst3', dst3)
cv2.waitKey()
cv2.destroyAllWindows()