import cv2, sys

# 이미지 불러오기
logo = cv2.imread('data2/opencv-logo-white.png', cv2.IMREAD_UNCHANGED)
dst = cv2.imread('data2/cat.bmp')
# 모든 행, 모든 열, 0~2번 채널
logo_ex = logo[:,:,:3]
# 알파 채널만 슬라이싱
mask = logo[:,:,3]
h, w = mask.shape[:2]
crop = logo[10:10+h, 10:10+w]

# 마스크 연산
cv2.copyTo(logo, mask, crop)

cv2.imshow('img', crop)
cv2.waitKey()
cv2.destroyAllWindows()