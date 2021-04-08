import cv2
import numpy as np 

img = cv2.imread("data/image10.jpeg")
kernel = np.ones((5, 5), dtype=np.uint8)
imgCanny = cv2.Canny(img, 50, 100)
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
imageEroded = cv2.erode(imgDilation, kernel, iterations=1)

cv2.imshow("Edge detection", imgCanny)
cv2.imshow("Image Dialation", imgDilation)
cv2.imshow("Image Erosion", imageEroded)

cv2.waitKey(0)
cv2.destroyAllWindows()