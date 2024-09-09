import cv2, sys

src = cv2.imread('./9_9_mission/9_9_mission_pic.png')
print(src.shape)
dst = cv2.resize(src, (192,192))

src_blur = cv2.blur(src, (5,5))

dst_blur = cv2.resize(src_blur, (192,192))

dst_ia = cv2.resize(src, (192,192), interpolation=cv2.INTER_AREA)

cv2.imshow('src',src)
cv2.imshow('dst',dst)
cv2.imshow('src_blur', src_blur)
cv2.imshow('dst_blur', dst_blur)
cv2.imshow('dst_ia', dst_ia)
cv2.waitKey()
cv2.destroyAllWindows()

#창의 이름이 안 보이는 경우 사각형 버튼을 눌러 창의 크기를 키우시면 됩니다.