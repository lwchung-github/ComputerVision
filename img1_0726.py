import cv2

img = cv2.imread('images/test1.jpg')

print(img) #B-G-R
print(img[100, 150])
print(img.item(100, 150, 1))
img[100:110, 100:110] = 0
img[120:130, 120:130, 0] = 255
img[140:150, 120:130] = [0, 0, 255]

roi = img[10:30, 20:60] //201 *401
# 等號前後的長寬高須一致

img[50:50+len(roi), 30:30+len(roi[0])] = roi
# 下面兩行等同於上面一行
h, w, a = roi.shape
img[50:50+h, 30:30+w] = roi

# cv2.namedWindow('test', cv2.WINDOW_NORMAL)

cv2.namedWindow('test', cv2.WINDOW_NORMAL)
cv2.imshow('test', img)

cv2.waitKey(0)
cv2.destroyAllWindows()