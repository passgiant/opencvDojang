import cv2, sys

src = cv2.imread('misson/03.png')
if src is None:
    sys.exit('Image load failed')

dst_csa = cv2.convertScaleAbs(src,0.8,1.0)
dst_fnmdc = cv2.fastNlMeansDenoisingColored(dst_csa,None,7,7,7,21)

cv2.imshow('dst_fnmdc', dst_fnmdc)
cv2.waitKey()
cv2.destroyAllWindows()