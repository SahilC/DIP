import cv2
import numpy as np

element_dilate = cv2.getStructuringElement(cv2.MORPH_RECT,( 2,2 ),( 0, 0))
element_close = cv2.getStructuringElement(cv2.MORPH_RECT,( 100,100 ),( 0, 0))

def find_directional_gradient(im, kernel, axis,bias):
    temp = cv2.filter2D(im,-1,kernel)
    if axis == 0:
        temp = np.cumsum(temp,axis=0)[-1]
    else:
        temp = np.cumsum(temp.T,axis=0)[-1]
    x = (np.sum(temp)*1.0/len(temp) - bias)
    temp2 = np.zeros(len(temp))
    temp2[temp > x] = 1
    temp2[temp < x] = 0
    # print len(temp2)
    return temp2

for i in xrange(1,6):
    im_original = cv2.imread('building_'+str(i)+'.jpg')
    im = cv2.cvtColor(im_original,cv2.COLOR_BGR2GRAY)
    im = cv2.equalizeHist(im)

    tempr = cv2.resize(im,(1000,700))
    tempr[tempr < 56] = 0
    # tempr[tempr > 100] = 255
    tempr = cv2.bilateralFilter(tempr, 10, 50,10)
    # tempr = cv2.blur(tempr,(3,3))
    # thres = cv2.erode(tempr,element_close)
    tempo = cv2.resize(im_original,(1000,700))

    # tempr[tempr > 200] = 255

    # kernel = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
    # vertical_gradient  = find_directional_gradient(tempr,kernel,0,0)
    # temp2 = np.zeros((tempr.shape[0],tempr.shape[1]),dtype=np.uint8)
    # for i in xrange(len(tempr)):
    #     temp2[i] = np.multiply(tempr[i],vertical_gradient)
    #
    # horizontal_gradient  = find_directional_gradient(tempr,kernel.T,1,0)
    # temp4  = np.zeros((tempr.shape[1],tempr.shape[0]),dtype=np.uint8)
    # im2 = tempr.copy()
    # im2 = im2.T
    # for i in xrange(len(im2)):
    #     temp4[i] = np.multiply(im2[i],horizontal_gradient)
    #
    # temp4 = temp4.T
    #
    # temp4 = cv2.bitwise_and(temp2,temp4)
    # temp4 = cv2.bitwise_and(tempr,temp4)

    # cv2.imshow("XYYZZ",temp4)
    # temp4 = cv2.bitwise_and(im,im,mask = temp4)

    # blur = cv2.blur(temp2,(3,3))
    # retval, thres = cv2.threshold(blur, 0, 256, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    # thres = cv2.bitwise_not(thres)
    # _,contour,_ = cv2.findContours(thres.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(thres, contour, -1,255,-1)
    # retval, labels = cv2.connectedComponents(thres)
    # output = np.zeros_like(labels, dtype=np.uint8)
    # cv2.normalize(labels, output, 0 , 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    # edges = cv2.medianBlur(blur,3)
    # edges = cv2.Canny(blur,45,50,apertureSize = 3)
    # lines = cv2.HoughLinesP( edges, 1, np.pi/180, 200, minLineLength=50,maxLineGap=10)
    # for i in xrange(len(lines)):
    #     l = lines[i][0]
    #     print l
    #     cv2.line( temp2, (l[0], l[1]),(l[2], l[3]),0, 3, 8)

    # temp3 = np.zeros((im.shape[0],im.shape[1]),dtype=np.uint8)
    # # retval, labels = cv2.connectedComponents(edges)
    # # print labels
    # # cv2.normalize(labels, temp3, 0 , 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    # _,contours,_ = cv2.findContours(edges, 1, 2)
    # cv2.drawContours(temp3,contours,-1,255,-1)
    # temp4 = cv2.bitwise_and(temp3,temp3,mask = temp4)
    # # temp4 = cv2.bitwise_and(im,temp3,mask = temp4)
    # # for cnt in contours:
    # #     area = cv2.contourArea(cnt)
    # #     x,y,w,h = cv2.boundingRect(cnt)
    # #     if h > 1.2*w and area > 5:
    # #         cv2.rectangle(im,(x,y),(x+w,y+h),0,2)
    # # print temp3
    # thres = cv2.erode(cv2.dilate(thres,element_dilate),element_close)
    # thes = cv2.dilate(thres,element_dilate)
    # edges = cv2.medianBlur(thes,3)
    # edges = cv2.Canny(thes,45,50,apertureSize = 3)
    # temp3 = cv2.resize(thres,(1000,700))

    edges = cv2.Canny(tempr,99,100,apertureSize = 3)
    _,contours,_ = cv2.findContours(edges.copy(), 1, 2)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        x,y,w,h = cv2.boundingRect(cnt)
        # print area
        #     print '========================'
        if h*1.0/w > 1 and h*1.0/w < 4 and w*h >= 1200 and w > 10 and w < 70 and h < 170:
            # print vertical_gradient[x]*horizontal_gradient[y]
        #     print vertical_gradient[x] + horizontal_gradient[y]
            # print area
            cv2.rectangle(tempo,(x,y),(x+w,y+h),(255,0,0),2)
    # edges = auto_canny(temp2)
    # temp3 = np.zeros((im.shape[0],im.shape[1]),dtype=np.uint8)
    # retval, labels = cv2.connectedComponents(edges)
    # print labels
    # output = np.zeros_like(labels, dtype=np.uint8)
    # cv2.normalize(labels, output, 0 , 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    cv2.imshow("XYYZZZ",tempo)
    cv2.waitKey(0)
