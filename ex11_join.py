import cv2
import numpy as np

img = cv2.imread('data/image10.jpg')
new_width = 320
scale_factor = new_width / img.shape[1]
new_height =  scale_factor * img.shape[0]
new_shape = (new_width, int(new_height))
imgResize = cv2.resize(img, new_shape)
img_hor = np.hstack((imgResize, imgResize))
img_ver = np.vstack((imgResize, imgResize))

cv2.imshow("Horizontal", img_hor)
cv2.imshow("Vertical", img_ver)
cv2.waitKey(0)