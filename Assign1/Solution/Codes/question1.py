import cv2
import numpy as np

im = cv2.imread('lena1.jpg')
im2 = cv2.imread('lena2.jpg')

red = (im[:,:,0] - im2[:,:,0])
green = (im[:,:,1] - im2[:,:,1])
blue = (im[:,:,2] - im2[:,:,2])

cv2.imwrite("red.png",red)
cv2.imwrite("green.png", green)
cv2.imwrite("blue.png", blue)
