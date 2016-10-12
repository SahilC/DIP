import cv2
import numpy as np
def grow_square(gray,thres,x,y):
	width = 0
	max_area = 0
	while(x+width <= thres.shape[0] and y+width <= thres.shape[1]):
		# print (x+width,thres.shape[0])
		# print (y+width,thres.shape[1])
		if not (thres[x:x+width+100,y:y+width+100] == 255).any():
			width += 100
			max_area = width**2
		else:
			break
	return (max_area,width)

for i in xrange(1,4):
	max_x = 0
	max_y = 0
	max_width = 0
	max_area = 0

	im = cv2.imread('cloud'+str(i)+'.jpg')
	gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
	gray = cv2.resize(gray,(700,500))
	retval, thres = cv2.threshold(gray.copy(), 150, 255, cv2.THRESH_OTSU)
	for i in xrange(0,thres.shape[0],100):
		for j in xrange(0,thres.shape[1],100):
			temp = grow_square(gray,thres,i,j)
			if temp[0] > max_area:
				max_area = temp[0]
				max_x = i
				max_y = j
				print (max_x,max_y)
				print max_area
				max_width = temp[1]
	# print (max_x,max_y)
	# print max_width
	cv2.rectangle(thres, (max_y,max_x), (max_y+max_width,max_x+max_width), 255)
	cv2.imshow("IMG",thres)
	cv2.waitKey(0)