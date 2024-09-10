import cv2
import numpy as np
from glob import glob
import os

def getImageList():
    basePath = os.getcwd()
    dataPath = os.path.join(basePath,'images')
    fileNames = glob(os.path.join(dataPath,'*.jpg'))
    return fileNames

def drawROI(cpy, corners_list):
    cpy = cpy.copy()
    line_c = (128, 128, 255)
    lineWidth = 2
    for corners in corners_list:
        cv2.rectangle(cpy, tuple(corners[0]), tuple(corners[1]), color=line_c, thickness=lineWidth)
    disp = cv2.addWeighted(img, 0.3, cpy, 0.7, 0)
    return disp
    
def onMouse(event, x, y, flags, param):
    global startPt, img, corners_list, cpy, txtWrData
    cpy = img.copy()
    if event == cv2.EVENT_LBUTTONDOWN:
        startPt = (x,y)
    elif event == cv2.EVENT_LBUTTONUP:
        corners = [startPt, (x,y)]
        corners_list.append(corners)
        txtWrData = str(corners_list)
        cpy = drawROI(cpy, corners_list)
        startPt = None
        cv2.imshow('label',cpy)
    elif event == cv2.EVENT_MOUSEMOVE:
        if startPt:
            temp_corners_list = corners_list + [[startPt, (x,y)]]
            cpy = drawROI(cpy, temp_corners_list)
            cv2.imshow('label',cpy)
        
corners_list = []
startPt = None
cpy = []
txtWrData = None

fileNames = getImageList()

img = cv2.imread(fileNames[0])

cv2.namedWindow('label')
cv2.setMouseCallback('label', onMouse, [img])
cv2.imshow('label', img)

while True:
    key = cv2.waitKey()
    if key == 27: # ESC
        break
    elif key == ord('s'):
        filename, ext = os.path.splitext(fileNames[0])
        txtFilename = filename + '.txt'
        with open(txtFilename, 'w') as f:
            for corners in corners_list:
                f.write(f"{corners}\n")
        print(f'Saved {len(corners_list)} boxes to {txtFilename}')
    elif key == ord('c'):  # 'c'를 누르면 모든 박스 초기화
        corners_list = []
        cpy = img.copy()
        cv2.imshow('label', cpy)
    
cv2.destroyAllWindows()