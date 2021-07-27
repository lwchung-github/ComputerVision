import cv2 as cv
import numpy as np

def nothing(x):
    pass

cv.namedWindow('img1')
cv.createTrackbar('A', 'img1', 0, 255, nothing)
cv.createTrackbar('B', 'img1', 0, 255, nothing)

cap = cv.VideoCapture(0)

while (True):
    ret, frame = cap.read()
    img2 = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    A = cv.getTrackbarPos('A', 'img1')
    B = cv.getTrackbarPos('B', 'img1')
    lower_blue = np.array([A, 50, 50])
    upper_blue = np.array([B, 255, 255])
    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(img2, lower_blue, upper_blue)
    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame, frame, mask = mask)

    cv.imshow('img',frame)
    cv.imshow('res',res)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

cap.release()    
cv.destroyAllWindows()