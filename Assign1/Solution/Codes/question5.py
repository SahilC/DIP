import cv2
import numpy as np
from collections import defaultdict
im = cv2.imread('lotus.jpg')

data = im.reshape((-1,3))
data = np.float32(data)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 5
ret,label,center = cv2.kmeans(data,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
 
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((im.shape))
count = defaultdict(int)
for i in label:
	count[i[0]] += 1
n = 0
mx_key = 0
mx_val = count[0]
print count
for k in count.keys():
	if count[k] > mx_val:
		mx_val = count[k]
		mx_key = k

print center[mx_key]
for i in center:
	radius = 40
	if center[mx_key][0] == i[0] and center[mx_key][1] == i[1] and center[mx_key][2] == i[2]:
		radius = 50
	cv2.circle(res2, (50+n,100),radius,(int(i[0]),int(i[1]),int(i[2])),cv2.FILLED,8,0)
	cv2.circle(res2, (50+n,100),radius+2,(0,0,0),2,0)
	n += 100
#print ret
cv2.GaussianBlur(res2,(5,5),10)
cv2.imwrite('kmeans.png',res2)
#cv2.waitKey(0)

# cv2.namedWindow("image")
# cv2.imshow("image",im)
# cv2.waitKey(0)