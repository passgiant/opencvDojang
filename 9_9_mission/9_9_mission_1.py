import cv2
import numpy as np

# 블러 함수 호출한 다음도 하기, 이미지 사이즈, 512, 512

img = np.ones((512,512,3), dtype=np.uint8)*255

pt_x = (0,0)
pt_y = (0,0)
poly_pt = []

def mouse_callback(event, x, y, flags, param):
    img = param[0]
    global pt_x, pt_y, poly_pt
    if event == cv2.EVENT_LBUTTONDOWN:
        if flags & cv2.EVENT_FLAG_SHIFTKEY:
            # pt_x = (x,y)
            poly_pt.append([x,y])
        else:
            poly_pt = np.array(poly_pt)
            cv2.polylines(img, [poly_pt], isClosed=True, color=(255,0,0))
            poly_pt = []
        #elif event == cv2.EVENT_LBUTTONUP:
        # pt_y = (x,y)
        # cv2.rectangle(img, pt_x, pt_y, (255,255,0), 2)
    elif event == cv2.EVENT_RBUTTONUP:
        pt_y = (x,y)
        cv2.circle(img, (x,y), 30, (0,255,0), 2)
        
    cv2.imshow('img',img)
    cv2.imwrite('./9_9_mission/9_9_mission_pic.png', img)

cv2.imshow('img',img)

cv2.setMouseCallback('img', mouse_callback, [img])

cv2.waitKey()
cv2.destroyAllWindows()