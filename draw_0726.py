import numpy as np
import cv2 as cv

img = cv.imread('images/test1.jpg')
print(len(img), len(img[0]))
print(img.shape)

cv.line(img, (0, 0), (183, 275), (0, 0, 255), 5)
# 參數: 圖片 起始點 結束點 顏色 線條租細

#-1: 填充
cv.rectangle(img, (100, 50), (150, 100), (255, 0, 0), -1)
cv.circle(img, (50, 50), 10, (0, 255, 0), -1)
cv.putText(img, 'hello world', (30, 40), 2, 1, (255, 255, 0))

pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv.polylines(img,[pts],True,(0,255,255))

cv.imshow('test', img)

k = cv.waitKey(0)

if k == 27:
    cv.destroyAllWindows()
else:
    cv.imwrite('test.png', img)
    cv.destroyAllWindows()
