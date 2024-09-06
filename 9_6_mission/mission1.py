import cv2, sys

src = cv2.imread('misson/01.png')
if src is None:
    sys.exit('Image load failed')
    
dst_fnmdc = cv2.fastNlMeansDenoisingColored(src,None,7,7,7,21)
dst_csa = cv2.convertScaleAbs(dst_fnmdc,0.6,0.6)

cv2.imshow('fnmdc', dst_fnmdc)
cv2.imshow('fnmdc+csa', dst_csa)
cv2.waitKey()
cv2.destroyAllWindows()