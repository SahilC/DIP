import cv2
import numpy as np
#
element = cv2.getStructuringElement(cv2.MORPH_RECT,( 1,1 ),( 0, 0))
# im = cv2.imread('soccer_1.png')
# cv2.imshow("XYZZZ",im[len(im)-100:len(im),1:100])

for i in xrange(1,10):
    im = cv2.imread('soccer_'+str(i)+'.png')
    # gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    #
    # temp = np.zeros((im.shape[0],im.shape[1]),dtype=np.uint8)
    # edges = cv2.Canny(gray,50,100,apertureSize = 3)
    # _,cnt,_ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    # cv2.drawContours(temp, cnt, -1, 255,cv2.FILLED)
    #
    # _,temp = cv2.threshold(temp, 128, 255, cv2.THRESH_BINARY)
    hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
    lower_green = np.array([40,16,25])
    upper_green = np.array([70,200,200])

    mask = cv2.inRange(hsv, lower_green, upper_green)
    mask = cv2.medianBlur(mask,3)

    retval, thres = cv2.threshold(mask, 150, 255, cv2.THRESH_BINARY)
    retval, labels = cv2.connectedComponents(thres)
    output = np.zeros_like(labels, dtype=np.uint8)
    cv2.normalize(labels, output, 0 , 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    counts = np.bincount(output.flatten())
    max_label = np.argmax(counts)
    output[output != max_label] = 0
    output[output == max_label] = 255

    #mask = cv2.bitwise_not(mask)
    #mask = cv2.bitwise_and(mask,mask,mask=temp)
    cv2.imshow('soccer_'+str(i)+'.png',output)
    cv2.waitKey(0)
