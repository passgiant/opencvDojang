import cv2, sys

src = cv2.imread('misson/05.png')
if src is None:
    sys.exit('Image load failed')

dst_csa = cv2.convertScaleAbs(src,0.8,0.7)

cv2.imshow('dst_csa', dst_csa)
cv2.waitKey()
cv2.destroyAllWindows()