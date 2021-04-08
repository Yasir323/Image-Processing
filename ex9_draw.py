import cv2
import numpy as np 

img = np.zeros((512, 512, 3), np.uint8) # Still a black image
# Draw a line
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)

# Rectangle
cv2.rectangle(img, (100, 100), (300, 300), (0, 0, 255), 3)

# Filled rectangle
# cv2.rectangle(img, (100, 100), (300, 300), (0, 0, 255), cv2.FILLED)

# Circle
cv2.circle(img, (400, 50), 50, (255, 255, 0), 5)

# Text
cv2.putText(img, "Hello World", (300, 400), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 255), 1)

cv2.imshow("Line", img)
cv2.waitKey(0)