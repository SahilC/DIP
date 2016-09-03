import cv2
import numpy as np
from Queue import Queue
im = cv2.imread('maze1.png')

def get_adj(pix):
	return [(pix[0]-1,pix[1]),(pix[0],pix[1]-1),(pix[0]+1,pix[1]),(pix[0],pix[1]+1)]

grid = (255-im[:,:,0])-(255-im[:,:,2])
start = (im.shape[0]-50,20)
end = (im.shape[0]/2,im.shape[1]/2)
queue = Queue()
queue.put([start])
final_path = []
while not queue.empty():
	path = queue.get()
	point = path[-1]
	if point == end:
		final_path = path
		break
	for points in get_adj(point):
		neighbourhood = (grid[points[0]-12:points[0]+12,points[1]-15:points[1]+15]).reshape((1,-1))
		if points[0] < im.shape[0] and points[1] < im.shape[1] and grid[points[0]][points[1]] == 0 and 255 not in neighbourhood:
			grid[points[0]][points[1]] = 127
			new_path = list(path)
			new_path.append(points)
			queue.put(new_path)

#grid = (255-im[:,:,0])-(255-im[:,:,2])
for pixel in final_path :
	#print pixel
	#print (grid[pixel[0]:pixel[0]+10,pixel[1]:pixel[1]+10]).reshape((1,-1))
	im[pixel[0]-12:pixel[0]+12,pixel[1]-15:pixel[1]+15]= (0,255,0)
	
	#im[pixel[0]][pixel[1]] = (127,127,0)

#print final_path
#cv2.imshow("image",im)
cv2.imwrite('maze.png',im)
#cv2.imshow("image",im)
cv2.waitKey(0)