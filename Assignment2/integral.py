import cv2
import numpy as np

im = cv2.imread('face.png')
img = cv2.cvtColor( im, cv2.COLOR_RGB2GRAY )
integral_im = cv2.integral(img)
print img
print integral_im
w,h = integral_im.shape
out = np.zeros((w,h))
for i in xrange(w):
    for j in xrange(h):
        if i == 0 and j == 0:
            out[i][j] = int(integral_im[i][j])
        elif i == 0:
            out[i][j] = int(integral_im[i][j]-integral_im[i][j-1])
        elif j == 0:
            out[i][j] = int(integral_im[i][j]-integral_im[i-1][j])
        else:
            out[i][j] = int(integral_im[i][j] - integral_im[i-1][j] - integral_im[i][j-1] + integral_im[i-1][j-1])

#out = cv2.cvtColor( out, cv2.COLOR_RGB2GRAY )
print out
cv2.imshow("Org",img)
cv2.imshow("Integral",out)
cv2.waitKey(0)
