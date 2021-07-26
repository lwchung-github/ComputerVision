import cv2

img = cv2.imread('images/test1.jpg')

# print(img) #B-G-R
cv2.namedWindow('test', cv2.WINDOW_NORMAL)
cv2.imshow('test', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('test.png', img)