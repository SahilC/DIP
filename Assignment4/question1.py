import cv2
import numpy as np
def grow_square(gray,thres,x,y,cache):
	width = 0
	max_area = 0
	#while(x+width <= thres.shape[0] and y+width <= thres.shape[1]):
	if not (thres[x:x+width+cache[y],y:y+width+cache[y]] == 255).any():
		if cache[y] != 0 and x+width + cache[y]<= thres.shape[0] and y+width+cache[y] <= thres.shape[1]:
			width += cache[y]
			max_area = width**2
	# 	else:
	# 		break
	# else:
	# 	break
	return (max_area,width)

def update_cache(thres,x,cache):
	# print len(cache)
	# for i in xrange(0,thres.shape[1]):
	# 	if thres[x,i] == 0:
	# 		cache[i] += 1
	# 	else:
	# 		cache[i] = 0
	cache[thres[x,] == 0] += 1
	cache[thres[x,] != 0] = 0

for i in xrange(1,4):
	max_x = 0
	max_y = 0
	max_width = 0
	max_area = 0

	im = cv2.imread('cloud'+str(i)+'.jpg')
	gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
	gray = cv2.resize(gray,(700,500))
	retval, thres = cv2.threshold(gray.copy(), 150, 255, cv2.THRESH_OTSU)
	cache = np.zeros(thres.shape[1],np.uint8)
	for i in xrange(thres.shape[0]-1,-1,-1):
		update_cache(thres,i,cache)
		for j in xrange(0,thres.shape[1],1):
			temp = grow_square(gray,thres,i,j,cache)
			if temp[0] >= max_area:
				max_area = temp[0]
				max_x = i
				max_y = j
				max_width = temp[1]
	print (max_y+max_width,max_x+max_width)
	im = cv2.resize(im,(700,500))
	cv2.rectangle(thres, (max_y,max_x), (max_y+max_width,max_x+max_width), 255)
	cv2.imshow("IMG",thres)
	cv2.waitKey(0)