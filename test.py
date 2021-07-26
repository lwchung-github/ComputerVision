import cv2

img = cv2.imread('images/test1.jpg')

# print(img) #B-G-R
# cv2.namedWindow('test', cv2.WINDOW_NORMAL)
cv2.imshow('test', img)

k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()
else:
    cv2.imwrite('test.png', img)
    cv2.destroyAllWindows()