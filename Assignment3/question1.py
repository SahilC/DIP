import cv2
import numpy as np

for i in xrange(1,11):
    im = cv2.imread('soccer_'+str(i)+'.png')
    hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
    lower_green = np.array([38,16,25])
    upper_green = np.array([70,200,200])
    mask = cv2.inRange(hsv, lower_green, upper_green)
    res = cv2.bitwise_and(im,im, mask= mask)
    cv2.imshow('soccer_'+str(i)+'.png',res)
    cv2.waitKey(0)
