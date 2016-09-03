import cv2
import numpy as np
im = cv2.imread('face.png')
X = im
g = []
for i in xrange(5):
  X = cv2.blur(X,(5,5))
  X = cv2.pyrDown(X)
  g.append(X)

Y = X
l = []
for i in xrange(4):
  temp = cv2.pyrUp(Y)
  l.append(g[3-i] - temp)
  cv2.imshow("IMAGE",l[i])
  cv2.waitKey(0)
  Y = g[3-i]
end
