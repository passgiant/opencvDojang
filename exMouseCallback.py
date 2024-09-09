import cv2, sys
import numpy as np

# 마우스 콜백 함수 구현
# 마우스에서 이벤트가 발생하면서 호출되는 함수
#버튼 클릭, 마우스 좌표를 이동
pt_x = (0,0)
pt_y = (0,0)

def mouse_callback(event, x, y, flags, param):
    #global img
    img = param[0]
    global pt_x, pt_y
    if event == cv2.EVENT_LBUTTONDOWN:
        # (x,y) 좌표에 반지름 5, 파란색, 색상은 꽉 채워서 원으로 그린다.
        #cv2.circle(img, (x,y), 10, (255,0,0), 2)
        pt_x = (x, y)
    elif event == cv2.EVENT_LBUTTONUP:
        pt_y = (x, y)
        cv2.rectangle(img, pt_x, pt_y, (255, 255, 0), 3)
    
    cv2.imshow('img', img)
    #     print('LButton Down!')
    # elif event == cv2.EVENT_LBUTTONUP:
    #     print('LButton Up!')
    # elif event == cv2.EVENT_MOUSEMOVE:
    #     print(f'x:{x}, y:{y}')

#흰색 캔버스를 생성
img = np.zeros((512,512,3), np.uint8)+255
img2 = np.ones((512,512,3), np.uint8)*255

cv2.imshow('img', img)

#메인에서 setMouseCallback함수를 실행하면서 콜백함수를 지정
cv2.setMouseCallback('img', mouse_callback, [img])

cv2.waitKey()
cv2.destroyAllWindows()