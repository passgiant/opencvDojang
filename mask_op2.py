import cv2, sys

# 이미지 불러오기
logo = cv2.imread('data2/opencv-logo-white.png', cv2.IMREAD_UNCHANGED)
dst = cv2.imread('data2/cat.bmp')

# 파일이 정상적으로 읽히지 않았다면
if dst is None or logo is None:
    sys.exit("Image Load failed!")

# 알파 채널만 슬라이싱
mask = logo[:,:,3]

# 모든 행, 모든 열, 0~2번 채널
src = logo[:,:,:3]

h, w = mask.shape[:2]
crop = dst[10:10+h, 10:10+w]

# 마스크 연산
cv2.copyTo(src, mask, crop)

cv2.imshow('img', dst)
cv2.waitKey()
cv2.destroyAllWindows()

# logo에서 BGR채널 가져오기
# src = logo[:,:,:-1]