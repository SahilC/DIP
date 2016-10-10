import cv2
import numpy as np
import math
# import matplotlib.pyplot as plt

def threshold(im , threshold = 150):
	im[im > threshold] = 255
	im[im < threshold] = 0

def getEccentricity(mu):
    return math.sqrt( ( mu['m20'] - mu['m02'] ) *  ( mu['m20'] - mu['m02'] )  + 4 * mu['m11'] * mu['m11'])

def otsu_threshold(im):
	vals = im.flatten()
	bins,_ = np.histogram(vals, 256)
	# _,bins,_ = plt.hist(vals, 255)
	p =  np.array(bins,dtype='float64')/sum(bins)
	sigma_b = np.zeros(256)
	for t in xrange(256):
		left = p[1 : t]
		right = p[t+1:]
		q_L = np.sum(left)
		q_H = np.sum(right)
		if(q_L > 0 and q_H > 0):
			miu_L = np.sum(np.multiply(left,range(1,t))) / q_L
			miu_H = np.sum(np.multiply(right,range(t + 1, 256))) / q_H
			sigma_b[t] = q_L * q_H * (miu_L - miu_H)**2
	t = np.argmax(sigma_b)
	return t

def sliding_window(image, stepSize, windowSize):
	for y in xrange(0, image.shape[0], stepSize):
		for x in xrange(0, image.shape[1], stepSize):
			yield (x, y, image[y:y + windowSize[1], x:x + windowSize[0]])

def adaptiveThreshold(im):
	new_im = np.zeros(im.shape,np.uint8)
	count = 0
	wh = 10
	ww = 10
	for (x, y, window) in sliding_window(im, stepSize=10, windowSize=(wh,ww)):
		if window.shape[0] != wh or window.shape[1] != ww:
			continue
		# v = np.var(window.flatten())
		m = np.mean(window.flatten())
		threshold(window,m - 10)
		new_im[y:y+ww,x:x+wh] = window
		# if v >= 5:
		# 	t = otsu_threshold(window)
		# 	threshold(window,t)
		# 	new_im[y:y+ww,x:x+wh] = window
		# else:
		# 	m = np.mean(window.flatten())
		# 	threshold(window,m - 20)
		# 	new_im[y:y+ww,x:x+wh] = window


	# for i in xrange(0,len(im),3):
	# 	lines = im[i:i+3]
	# 	for j in xrange(0,len(lines[0]),3):
	# 		vals = []
	# 		vals.append(lines[0][j:j+3])
	# 		vals.append(lines[1][j:j+3])
	# 		vals.append(lines[2][j:j+3])
	# 		vals = np.array(vals)
	# 		var = np.var(vals.flatten())
	# 		if var > 1:
	# 			t = otsu_threshold(vals)
	# 			threshold(vals,t)
	# 			new_im[i][j] = vals[0][0]
	# 			new_im[i+1][j] = vals[1][0]
	# 			new_im[i+2][j] = vals[2][0]
	# 			new_im[i+1][j+1] = vals[1][1]
	# 			new_im[i+1][j+2] = vals[1][2]
	# 			new_im[i][j+1] = vals[0][1]
	# 			new_im[i+2][j] = vals[2][0]
	# 			new_im[i+2][j+1] = vals[2][1]
	# 			new_im[i+2][j+2] = vals[2][2]
	# 		else:
	# 			if(np.mean(vals.flatten()) > 100):
	# 				new_im[i][j] = vals[0][0]
	# 				new_im[i+1][j] = vals[1][0]
	# 				new_im[i+2][j] = vals[2][0]
	# 				new_im[i+1][j+1] = vals[1][1]
	# 				new_im[i+1][j+2] = vals[1][2]
	# 				new_im[i][j+1] = vals[0][1]
	# 				new_im[i+2][j] = vals[2][0]
	# 				new_im[i+2][j+1] = vals[2][1]
	# 				new_im[i+2][j+2] = vals[2][2]

	return new_im




for i in xrange(1,4):
	im = cv2.imread('document'+str(i)+'.jpg')
	im = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

	im = cv2.blur(im,(5,5))
	im = cv2.resize(im,(500,700))
	im = adaptiveThreshold(im)
	thres = cv2.bitwise_not(im)
	_,contours,_ = cv2.findContours(thres.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
	new_im = np.zeros(im.shape,np.uint8)
	for cnt in contours:
		# M = cv2.moments(cnt)
		# e = getEccentricity(M)
		x,y,w,h = cv2.boundingRect(cnt)
		if float(w)/h > 1:
			cv2.drawContours(new_im, [cnt], -1,255,1)

	dilate = cv2.getStructuringElement(cv2.MORPH_RECT,( 15,15 ),( 0, 0))
	new_im = cv2.dilate(new_im,dilate)

	out = cv2.bitwise_and(new_im,thres)

	cv2.imshow("XYYZZZ",out)
	cv2.waitKey(0)
