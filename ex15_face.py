import cv2

face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')
img = cv2.imread('data/melissa.jpg')
new_width = 320
scale_factor = new_width / img.shape[1]
new_height =  scale_factor * img.shape[0]
new_shape = (new_width, int(new_height))
img = cv2.resize(img, new_shape)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(img_gray, 1.3, 5)
for (x, y, w, h) in faces:
	cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 255), 2)

cv2.imshow('Result', img)
cv2.waitKey(0)