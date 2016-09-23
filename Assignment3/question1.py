import cv2
import numpy as np
#
element_dilate = cv2.getStructuringElement(cv2.MORPH_RECT,( 50,50 ),( 0, 0))
element_close = cv2.getStructuringElement(cv2.MORPH_RECT,( 50,50 ),( 0, 0))
# im = cv2.imread('soccer_1.png')
# cv2.imshow("XYZZZ",im[len(im)-100:len(im),1:100])

for i in xrange(1,10):
    im = cv2.imread('soccer_'+str(i)+'.png')

    hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
    lower_green = np.array([37,16,70])
    upper_green = np.array([56,256,256])

    mask = cv2.inRange(hsv, lower_green, upper_green)
    mask = cv2.medianBlur(mask,3)

    retval, thres = cv2.threshold(mask, 150, 255, cv2.THRESH_OTSU)
    retval, labels = cv2.connectedComponents(thres)
    output = np.zeros_like(labels, dtype=np.uint8)
    cv2.normalize(labels, output, 0 , 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    counts = np.bincount(output.flatten())
    max_label = np.argmax(counts)
    output[output != max_label] = 0
    output[output == max_label] = 255

    #print counts
    output = cv2.bitwise_not(output)
    #output = cv2.erode(cv2.dilate(output,element_dilate),element_close)
    ret,image_thresh = cv2.threshold(output, 125, 255, cv2.THRESH_BINARY)
    _,contour,_ = cv2.findContours(image_thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    #output = cv2.drawContours(output.copy(),contour,0,150,cv2.FILLED)
    img = np.zeros( (im.shape[0],im.shape[1]))
    cv2.drawContours(img, contour[:-2], -1,255,-1)

    #print cv2.convexHull(output)
    # im = cv2.blur(im,(3,3))
    # gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    # temp = np.zeros((im.shape[0],im.shape[1]),dtype=np.uint8)
    # edges = cv2.Canny(gray,50,100,apertureSize = 3)
    # _,cnt,_ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    # cv2.drawContours(temp, cnt, -1, 255,cv2.FILLED)
    #
    # _,temp = cv2.threshold(temp, 128, 255, cv2.THRESH_BINARY)
    #mask = cv2.bitwise_and(im,im,mask=mask)
    cv2.imshow('soccer_'+str(i)+'.png',img)
    cv2.waitKey(0)
