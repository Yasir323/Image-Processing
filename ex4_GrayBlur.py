import cv2

img = cv2.imread("data/image10.jpeg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (7, 7), 0)
cv2.imshow("Original Image", img)
cv2.imshow("Gray Image", img_gray)
cv2.imshow("Blurred Image", img_blur)
cv2.waitKey(0)