import cv2
import numpy as np
from glob import glob
import os

def getImageList():
    basePath = os.getcwd()
    dataPath = os.path.join(basePath,'images')
    fileNames = glob(os.path.join(dataPath,'*.jpg'))
    return fileNames

def drawROI(cpy, boxList, currentBox=None):
    cpy = cpy.copy()
    line_c = (128, 128, 255)
    lineWidth = 2
    for corners in boxList:
        cv2.rectangle(cpy, tuple(corners[0]), tuple(corners[1]), color=line_c, thickness=lineWidth)
    if currentBox:
        cv2.rectangle(cpy, tuple(currentBox[0]), tuple(currentBox[1]), color=(0, 255, 0), thickness=lineWidth)
    disp = cv2.addWeighted(img, 0.3, cpy, 0.7, 0)
    return disp

def onMouse(event, x, y, flags, param):
    global startPt, img, boxList, cpy, txtWrData
    if event == cv2.EVENT_LBUTTONDOWN:
        startPt = (x,y)
    elif event == cv2.EVENT_LBUTTONUP:
        if startPt:
            ptList = [startPt, (x,y)]
            boxList.append(ptList)
            txtWrData = str(boxList)
            cpy = drawROI(img, boxList)
            startPt = None
            cv2.imshow('label', cpy)
    elif event == cv2.EVENT_MOUSEMOVE:
        if startPt:
            currentBox = [startPt, (x,y)]
            cpy = drawROI(img, boxList, currentBox)
            cv2.imshow('label', cpy)

boxList = []
startPt = None
cpy = None
txtWrData = None

fileNames = getImageList()
img = cv2.imread(fileNames[0])

cv2.namedWindow('label')
cv2.setMouseCallback('label', onMouse)
cv2.imshow('label', img)

while True:
    key = cv2.waitKey(1)
    if key == 27: # ESC
        break
    elif key == ord('s'):
        filename, ext = os.path.splitext(fileNames[0])
        txtFilename = filename + '.txt'
        with open(txtFilename, 'w') as f:
            f.write(txtWrData)
        print(f'Saved to {txtFilename}: {txtWrData}')
    elif key == ord('c'): # c키를 누르면 모든 박스 초기화
        boxList = []
        cpy = img.copy()
        cv2.imshow('label', cpy)

cv2.destroyAllWindows()