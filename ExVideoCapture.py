import cv2, sys

fileName = 'data/vtest.avi'

# VideoCapture 클래스 객체 생성 + 생성자가 호출(파일 열기)
cap = cv2.VideoCapture(fileName)

frameSize = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(frameSize)

while True:
    retval, frame = cap.read()
    # retval가 양수가 아니면 while문 빠져나가기(종료)
    if not retval:
        break
    cv2.imshow('frame', frame)
    # 100ms 대기 (이 동영상은 초당 10프레임 짜리니까)
    key = cv2.waitKey(100)
    # 키 입력이 ESC(27)이면 종료
    if key == 27:
        break
    
# 동영상을 열었으면, 닫아야 한다.
if cap.isOpened():
    cap.release() # 열림 해제
    
cv2.destroyAllWindows()