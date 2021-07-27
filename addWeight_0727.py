import cv2

img = cv2.imread('images/test1.jpg')
print(img.shape)
roi1 = img[100:110, 100:120]
roi2 = img[120:130, 120:140]
dst = cv2.addWeighted(roi1, 0.7, roi2, 0.3, 0)

img[50:60, 30:50] = dst

# cv2.namedWindow('test', cv2.WINDOW_NORMAL)

cv2.namedWindow('test', cv2.WINDOW_NORMAL)
cv2.imshow('test', img)

cv2.waitKey(0)
cv2.destroyAllWindows()