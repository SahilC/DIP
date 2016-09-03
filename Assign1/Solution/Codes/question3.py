import cv2
import numpy as np
import math

refPt = []
mode = 'Line'
def click_and_crop(event, x, y, flags, param):
	global refPt, im, mode, result_img

	if event == cv2.EVENT_LBUTTONDOWN:
		refPt = [(x, y)]

	elif event == cv2.EVENT_LBUTTONUP:
		refPt.append((x, y))
		print refPt
		height,width,depth = im.shape
		if mode == 'Line':
			#cv2.line(im, refPt[0], refPt[1], (0, 255, 0), 3)
			cv2.imshow("image", im)
			
			sub_region = im[refPt[0][0]+50:refPt[1][0]+50,refPt[0][1]-200:refPt[1][1]+300]
	 		im = cv2.GaussianBlur(im,(11,11),30)
	 		im[refPt[0][0]+50:refPt[1][0]+50,refPt[0][1]-200:refPt[1][1]+300] = sub_region
	 	else:
	 		radius = math.sqrt((refPt[0][0]-refPt[1][0])**2 + (refPt[0][1]-refPt[1][1])**2)
	 		#cv2.circle(im,refPt[0],int(radius),(0,255,0),3)
	 		cX = refPt[0][0]
			cY = refPt[0][1]
			result_img = cv2.GaussianBlur(result_img,(11,11),30)
			height,width,depth = im.shape
			circle_img = np.zeros((height,width), np.uint8)
			cv2.circle(circle_img,(width/2,height/2),280,1,thickness=-1)
			masked_image = cv2.bitwise_and(im, im, mask=circle_img)
			masked_data = cv2.bitwise_and(result_img, result_img, mask=(1-circle_img))
			result_img = cv2.add(masked_image,masked_data)
			im = result_img
			maxDistance = math.sqrt (cY**2 + cX**2)
	
			for i in xrange(height):
				for j in xrange(width):
					dis = math.sqrt ((i-cY)**2 + (j-cX)**2)
					scale_val = (1-0.8*dis/maxDistance) if (1-0.8*dis/maxDistance) > 0 else 0
					result_img[i][j][0] = im[i][j][0]*scale_val
					result_img[i][j][1] = im[i][j][1]*scale_val
					result_img[i][j][2] = im[i][j][2]*scale_val

			im = result_img


im = cv2.imread('car.png')
result_img = im.copy()

cv2.namedWindow("image")
cv2.setMouseCallback("image", click_and_crop)

while True:
	cv2.imshow("image",im)
	#cv2.putText(im,"Mode:"+mode+" - Press m to toggle.", (10,19), cv2.FONT_HERSHEY_SIMPLEX, 1, 255)
	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
		break
	elif key == ord("m"):
		cv2.imwrite('car_'+mode+'.png',im)
		mode = 'Line' if mode == 'Circle' else 'Circle'



