import numpy as np
import cv2 as cv

# 鼠标回调函数
def draw_circle(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img,(x,y),50,(0,255,0),3)

def draw_rectangle(event,x,y,flags,param):
    if event == cv.EVENT_RBUTTONDBLCLK:       
        cv.rectangle(img, (x-30, y-10), (x+30, y+10), (255, 0, 0), 3)

def draw_picture(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img,(x,y),50,(0,255,0),3)
    if event == cv.EVENT_RBUTTONDBLCLK:       
        cv.rectangle(img, (x-30, y-10), (x+30, y+10), (255, 0, 0), 3)

img = cv.imread('images/test1.jpg')
cv.namedWindow('image', cv.WINDOW_AUTOSIZE)

# cv.setMouseCallback('image', draw_circle)
# cv.setMouseCallback('image', draw_rectangle)
cv.setMouseCallback('image', draw_picture)
while(1):
    cv.imshow('image',img)
    # 按esc結束
    if cv.waitKey(20) & 0xFF == 27:
        break
cv.destroyAllWindows()

'''
cv.imshow('test', img)
cv.waitKey(0)
cv.destroyAllWindows()
'''
'''
while(1):
    cv.imshow('image',img)
    if cv.waitKey(20) & 0xFF == 27:
        break
cv.destroyAllWindows()
'''
