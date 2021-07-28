import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/test1.jpg')
img1 = cv2.imread('images/test1.jpg',0)
cv2.namedWindow('image')

# min = cv2.getTrackbarPos('min','image')
# max = cv2.getTrackbarPos('max','image')
# edges = cv2.Canny(img, min, max)
edges = cv2.Canny(img,50,150)
lines = cv2.HoughLinesP(edges,1,np.pi/180,300,minLineLength=300,maxLineGap=20)
img2 = cv2.cvtColor(edges,cv2.COLOR_GRAY2BGR)

for line in lines:
    x1,y1,x2,y2 = line[0]
    cv2.line(img2,(x1,y1),(x2,y2),(0,255,0),2)

# edges2 = cv2.bitwise_and(img,img,mask=edges)
cv2.imshow('canny1',edges)
# cv2.imshow('canny2',edges1)
# cv2.imshow('edge2',edges2)
cv2.imshow('Line',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()