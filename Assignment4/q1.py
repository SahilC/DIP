import cv2
import numpy as np


for i in xrange(1,4):
	max_x = 0
	max_y = 0
	max_width = 0
	max_area = 0

	im = cv2.imread('cloud'+str(i)+'.jpg')
	gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
	gray = cv2.resize(gray,(700,500))
	retval, thres = cv2.threshold(gray.copy(), 150, 255, cv2.THRESH_OTSU)
	thres = cv2.bitwise_not(thres)
	cache = np.zeros(thres.shape,np.uint8)

	for i in xrange(thres.shape[0]):
		if(thres[i,0] == 255): 
			cache[i,0] = 1

	for j in xrange(thres.shape[0]):
		if(thres[0,j] == 255):
			cache[0,j] = 1

	for i in xrange(thres.shape[0]):
		for j in xrange(thres.shape[1]):
			if(thres[i,j] == 255): 
				cache[i,j] = min(cache[i,j-1], cache[i-1,j], cache[i-1,j-1]) + 1
			else:
				cache[i,j] = 0

	index = np.unravel_index(np.argmax(cache), cache.shape)
	max_width = cache[index[0],index[1]]
	im = cv2.resize(im,(700,500))
	cv2.rectangle(im, (index[1]-max_width,index[0]-max_width), (index[1],index[0]), (0,0,255))
	cv2.imshow("IMG",im)
	cv2.waitKey(0)