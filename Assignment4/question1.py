import cv2
import numpy as np
def grow_square(gray,thres,x,y,cachex,cachey):
	max_area = 0

	cache = max(cachex[y],cachey[x])
	if cache != 0 and not (thres[x:x+cache,y:y+cache] == 255).any() and ( x+cache < thres.shape[0] and y+cache < thres.shape[1]):
		width = cache
	else:
		cache = min(cachex[y],cachey[x])
		if cache != 0 and not (thres[x:x+cache,y:y+cache] == 255).any() and ( x+cache < thres.shape[0] and y+cache < thres.shape[1]):
			width = cache
		else:
			width = 0

	#while ( x+width < thres.shape[0]-1 and y+width < thres.shape[1]-1) and (not (thres[x:x+width+1,y:y+width+1] == 255).any()):
	if ( x+width < thres.shape[0] and y+width < thres.shape[1]) and (not (thres[x:x+width+1,y:y+width+1] == 255).any()):
		width += 1

	max_area = width**2
	return (max_area,width)

def update_cachex(thres,x,cache):
	# print len(cache)
	# for i in xrange(0,thres.shape[1]):
	# 	if thres[x,i] == 0:
	# 		cache[i] += 1
	# 	else:
	# 		cache[i] = 0
	cache[thres[x,] == 0] += 1
	cache[thres[x,] != 0] = 0

def update_cachey(thres,y,cache):
	# print len(cache)
	# for i in xrange(0,thres.shape[1]):
	# 	if thres[x,i] == 0:
	# 		cache[i] += 1
	# 	else:
	# 		cache[i] = 0
	cache[thres[:,y] == 0] += 1
	cache[thres[:,y] != 0] = 0

for i in xrange(1,4):
	max_x = 0
	max_y = 0
	max_width = 0
	max_area = 0

	im = cv2.imread('cloud'+str(i)+'.jpg')
	gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
	gray = cv2.resize(gray,(700,500))
	retval, thres = cv2.threshold(gray.copy(), 150, 255, cv2.THRESH_OTSU)
	cachex = np.zeros(thres.shape[1],np.uint8)
	cachey = np.zeros(thres.shape[0],np.uint8)
	k = thres.shape[1]-1
	for i in xrange(thres.shape[0]-1,-1,-1):
		update_cachex(thres,i,cachex)
		update_cachey(thres,k,cachey)
		k -= 1
		if k < 0:
			break
		for j in xrange(thres.shape[1]-1,-1,-1):
			temp = grow_square(gray,thres,i,j,cachex,cachey)
			if temp[0] >= max_area:
				max_area = temp[0]
				max_x = i
				max_y = j
				max_width = temp[1]
	print (max_y+max_width,max_x+max_width,max_width)
	im = cv2.resize(im,(700,500))
	cv2.rectangle(thres, (max_y,max_x), (max_y+max_width,max_x+max_width), 255)
	cv2.imshow("IMG",thres)
	cv2.waitKey(0)