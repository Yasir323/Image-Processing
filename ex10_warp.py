import cv2
import math
import numpy as np

img = cv2.imread('data/image20.jpg')

height = int(math.dist([267, 53], [166, 279]))
width = int(math.dist([267, 53], [433, 114]))
pts1 = np.float32([[267, 53], [166, 279], [338, 348], [433, 114]])
pts2 = np.float32([[0, 0], [0, height], [width, height], [width, 0]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
img_out = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow('Image', img)
cv2.imshow('Warped Image', img_out)
cv2.waitKey(0)