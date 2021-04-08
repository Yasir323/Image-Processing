import cv2 

img = cv2.imread('data/image10.jpg')
print(img.shape)

img_cropped = img[0:200, 200:500] # Height comes first then the width
cv2.imshow("Cropped image", img_cropped)
cv2.imshow("Original image", img)
cv2.waitKey(0)