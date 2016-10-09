import cv2
import numpy as np

im = cv2.imread('bottles.tif')
gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
mask = cv2.blur(gray,(3,3))
mask1 = np.zeros((im.shape[0],im.shape[1]),dtype=np.uint8)
mask2 = np.zeros((im.shape[0],im.shape[1]),dtype=np.uint8)
mask1[mask < 210] = 255
mask2[mask > 20] = 255
mask = cv2.bitwise_and(mask1,mask2)
kernel = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])

temp = cv2.filter2D(mask,-1,kernel)
temp = cv2.medianBlur(temp,3)

element_erode = cv2.getStructuringElement(cv2.MORPH_RECT,( 2,2 ),( 0, 0))
temp = cv2.erode(temp,element_erode)

_,contour,_ = cv2.findContours(temp.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
y_list = []
for cnt in contour:
	x,y,w,h = cv2.boundingRect(cnt)
	y_list.append(y)

y_mid = np.mean(np.array(y_list))
# print y_mid
mask1 = np.zeros((temp.shape[0]+2,temp.shape[1]+2),np.uint8)
for cnt in contour:
	x,y,w,h = cv2.boundingRect(cnt)
	if y > y_mid and w*h > 100:
		print x,y,w,h
		#cv2.drawContours(im, [cnt], -1,(255,0,0),-1)
		cv2.floodFill(mask, mask1,(x,y),255)
	else:
		cv2.floodFill(mask, mask1,(x,y),0)

im[:,:,0] = cv2.bitwise_and(im[:,:,0],mask)
im[:,:,1] = cv2.bitwise_and(im[:,:,1],mask)
im[:,:,2] = cv2.bitwise_and(im[:,:,2],mask)
cv2.imshow("XYYZZZ",im)
cv2.waitKey(0)
