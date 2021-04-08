import cv2
import numpy as np 

# A black grayscale image
img_grayscale = np.zeros((512, 512), dtype=np.uint8)
print(img_grayscale)
img_color = np.zeros((512, 512, 3), np.uint8) # Still a black image
img_color[:] = 255, 0, 0 # Whole image turns blue
img_color[100:200, 200:300] = 0, 255, 0 # A green patch in the middle
cv2.imshow("Grayscale", img_grayscale)
cv2.imshow("Colored", img_color)
print(img_color)
cv2.waitKey(0)