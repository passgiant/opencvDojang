import numpy as np
import cv2

img = np.full((400, 400, 3), 255, np.uint8)

# line
# pt1 = (50, 100)
# pt2 = (img.shape[0]-50, 100)
# pt3 = (img.shape[0]-50, 300)
# lineColor = (0, 0, 255)
# thick = 3
# lineType = cv2.LINE_8
# cv2.line(img, pt1, pt2, lineColor, thick, lineType)
# cv2.line(img, pt1, pt3, lineColor, thick, cv2.LINE_AA)

# putText
# text = 'Hello OPENCV!'
# font = cv2.FONT_HERSHEY_SIMPLEX
# fontsize = 1
# bluecolor = (255, 0, 0)
# thick = 2
# linetype = cv2.LINE_AA

# cv2.putText(img, text, (50,350), font, fontsize, bluecolor, thick, linetype)

# rectangle 1
# pt1 = (50, 100)
# pt2 = (img.shape[0]-50, 100)
# pt3 = (img.shape[0]-50, 300)
# pt4 = (200, 300)
# lineColor = (0, 0, 255)
# thick = 3
# lineType = cv2.LINE_AA
# cv2.rectangle(img, pt1, pt4, lineColor, thick)


# rectangle 2
# lineColor2 = (255, 0, 0)
# cv2.rectangle(img, (50, 100, 100, 100), lineColor2, thick, lineType)

# circle
cv2.circle(img, (int(img.shape[0]/2), int(img.shape[1]/2)), 100, (0, 255, 0), 2, cv2.LINE_AA)
# thick를 -1로 넣으면 색깔을 채움

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()