import cv2
import numpy as np

def auto_canny(image, sigma=0.01):
	# compute the median of the single channel pixel intensities
	v = np.mean(image)

	# apply automatic Canny edge detection using the computed median
	lower = int(max(0, (1.0 - sigma) * v))
	upper = int(min(255, (1.0 + sigma) * v))
	edged = cv2.Canny(image, lower, upper)

	# return the edged image
	return edged

element_dilate = cv2.getStructuringElement(cv2.MORPH_RECT,( 2,2 ),( 0, 0))
element_close = cv2.getStructuringElement(cv2.MORPH_RECT,( 20,20 ),( 0, 0))

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
    # gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    # edges = cv2.Canny(gray,70,100,apertureSize = 3)
    # edges = cv2.resize(edges,(1000,700))
    # hist = cv2.calcHist([im],[0],None,[256],[0,256])


    # a = np.fft.fft2(im)
    # a = np.fft.fftshift(a)
    # magnitude_spectrum = 20*np.log(np.abs(a))
    # plt.subplot(121),plt.imshow(im, cmap = 'gray')
    # plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    # plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
    # plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    # plt.show()
    # plt.hist(im.ravel(),256,[0,256]); plt.show()

    #y = cv2.resize(temp,(1000,700))
    #cv2.imshow('building_'+str(i)+'.png',y)
    kernel = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
    temp  = find_directional_gradient(im,kernel,0,0)
    temp2 = np.zeros((im.shape[0],im.shape[1]),dtype=np.uint8)
    for i in xrange(len(im)):
        temp2[i] = np.multiply(im[i],temp)

    temp3  = find_directional_gradient(im,kernel.T,1,0)
    temp4  = np.zeros((im.shape[1],im.shape[0]),dtype=np.uint8)
    im2 = im.copy()
    im2 = im2.T
    for i in xrange(len(im2)):
        temp4[i] = np.multiply(im2[i],temp3)

    temp4 = temp4.T

    temp4 = cv2.bitwise_and(temp2,temp4)

    #cv2.imshow("XYYZZ",temp2)
    # temp4 = cv2.bitwise_and(im,im,mask = temp4)
    # temp2 = cv2.resize(im,(1000,700))
    # temp4 = cv2.resize(im_original,(1000,700))
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
    # temp2[temp2 > 70] = 255
    # edges = cv2.Canny(temp2,99,100,apertureSize = 3)
    # _,contours,_ = cv2.findContours(edges, 1, 2)
    # for cnt in contours:
    #     area = cv2.contourArea(cnt)
    #     x,y,w,h = cv2.boundingRect(cnt)
    #     if h > w and area > 100:
    #         cv2.rectangle(temp4,(x,y),(x+w,y+h),(255,0,0),2)
    # edges = auto_canny(temp2)
    # temp3 = np.zeros((im.shape[0],im.shape[1]),dtype=np.uint8)
    # retval, labels = cv2.connectedComponents(edges)
    # print labels
    # output = np.zeros_like(labels, dtype=np.uint8)
    # cv2.normalize(labels, output, 0 , 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    cv2.imshow("XYYZZZ",temp4)
    cv2.waitKey(0)
