import cv2
import numpy as np

element_dilate = cv2.getStructuringElement(cv2.MORPH_RECT,( 2,2 ),( 0, 0))
element_close = cv2.getStructuringElement(cv2.MORPH_RECT,( 20,20 ),( 0, 0))

def find_directional_gradient(im, kernel, axis,bias):
    temp = cv2.filter2D(im,-1,kernel)
    if axis == 0:
        temp = np.cumsum(temp,axis=0)[-1]
    else:
        temp = np.cumsum(temp.T,axis=0)[-1]
    # x = (np.sum(temp)*1.0/len(temp) - bias)
    # temp2 = np.zeros(len(temp))
    # temp2[temp > x] = 1
    # temp2[temp < x] = 0
    # print len(temp2)
    return temp

for i in xrange(1,6):
    im_original = cv2.imread('building_'+str(i)+'.jpg')
    im = cv2.cvtColor(im_original,cv2.COLOR_BGR2GRAY)
    im = cv2.equalizeHist(im)

    tempr = cv2.resize(im,(1000,700))
    tempr[tempr > 70] = 255

    dst = cv2.cornerHarris(tempr,2,3,0.04)
    # dst = cv2.dilate(dst,None)
    # dst = np.array(dst,dtype=np.uint8)
    tempo = cv2.resize(im_original,(1000,700))
    # tempo[dst>0.01*dst.max()]=[0,0,255]
    _,contours,_ = cv2.findContours(dst.copy(), 1, 2)
    for cnt in contours:
        cv2.rectangle(tempo,(x,y),(x+w,y+h),(255,0,0),2)
    # print dst
    # temp3 = np.zeros((tempr.shape[0],tempr.shape[1]),dtype=np.uint8)
    # temp3 = cv2.cornerHarris(tempr,4,3)
    # threshold(dst, threshed, 0.00001, 255, THRESH_BINARY_INV)
    cv2.imshow("XYYZZZ",tempo)
    cv2.waitKey(0)
