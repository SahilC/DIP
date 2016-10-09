import cv2
import numpy as np
import math

def get_board(zero_points,cross_points):
	board = [['' for j in xrange(3)] for i in xrange(3)]
	for x in zero_points:
		if x[0] > 450:
			row = 2
		elif x[0] < 450 and x[0] > 300:
			row = 1
		elif x[0] < 300:
			row = 0

		if x[1] > 450:
			col = 2
		elif x[1] < 450 and x[1] > 300:
			col = 1
		elif x[1] < 300:
			col = 0
		board[col][row] = 'O'

	for x in cross_points:
		if x[0] > 450:
			row = 2
		elif x[0] < 450 and x[0] > 300:
			row = 1
		elif x[0] < 300:
			row = 0

		if x[1] > 450:
			col = 2
		elif x[1] < 450 and x[1] > 300:
			col = 1
		elif x[1] < 300:
			col = 0
		board[col][row] = 'X'
	return board

def board_wins(board):
	winner = ''
	for i in xrange(3):
		elem = board[i][0]
		val = True
		for j in xrange(3):
			if board[i][j] != elem:
				val = False
				break
		if val:
			winner = elem
			break

	for i in xrange(3):
		elem = board[0][i]
		val = True
		for j in xrange(3):
			if board[j][i] != elem:
				val = False
				break
		if val:
			winner = elem
			break

	elem = board[0][0]
	val = True
	for i in xrange(3):
		if board[i][i] != elem:
			val = False
			break
	if val:
		winner = elem

	elem = board[0][0]
	val = True
	for i in xrange(3):
		if board[i][2-i] != elem:
			val = False
			break
	if val:
		winner = elem
	return winner
		

for i in xrange(1,5):
	im = cv2.imread('tic-tac-toe'+str(i)+'.jpg')
	gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
	retval, thres = cv2.threshold(gray.copy(), 150, 255, cv2.THRESH_OTSU)
	thres = cv2.bitwise_not(thres)
	_,contours,_ = cv2.findContours(thres,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
	cross_points  = set()
	zero_points = set()
	for cnt in contours:
		hull =  cv2.convexHull(cnt,returnPoints = False )
		defects = cv2.convexityDefects(cnt,hull)
		M = cv2.moments(cnt)
		cx = int(M['m10']/M['m00'])
		cy = int(M['m01']/M['m00'])
		if defects != None and len(defects) <= 8 :
			cross_points.add((cx,cy))
		elif defects != None and len(defects) == 40:
			zero_points.add((cx,cy))			
			#cv2.drawContours(im, [cnt], -1,(255,0,0),5)
		# if defects != None and :
		# 	#print cnt
		# 	cv2.drawContours(im, [cnt], -1,(255,255,0),5)
	zero_points = list(zero_points)
	board = get_board(zero_points,cross_points)
	winner = board_wins(board)
	for cnt in contours:
		hull =  cv2.convexHull(cnt,returnPoints = False )
		defects = cv2.convexityDefects(cnt,hull)
		if defects != None and len(defects) <= 8 and winner == 'X':
			cv2.drawContours(im, [cnt], -1,(255,0,0),5)
		elif defects != None and len(defects) == 40 and winner == 'O':
			cv2.drawContours(im, [cnt], -1,(255,0,0),5)


	
	# vec_diff = []
	# cross_points = list(cross_points)
	# # print cross_points
	# for x in xrange(len(cross_points)-1):
	# 	vec_diff.append(float(math.fabs(cross_points[x+1][1] - cross_points[x][1]))/math.fabs(cross_points[x+1][0] - cross_points[x][0])) 
	
	# print "============"

	# for x in xrange(len(vec_diff)-1):
	# 	if (math.fabs(vec_diff[x+1][0] - vec_diff[x][0])) < 10 or math.fabs(vec_diff[x+1][1] - vec_diff[x][1]) < 10:
	# 		print "X wins"
	# 		break
	cv2.imshow("XYYZZZ",im)
	cv2.waitKey(0)