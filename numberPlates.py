import cv2

min_area = 500

car = cv2.imread('data/car1.jpeg')
image_width = car.shape[0]
image_height = car.shape[1]
number_plate_cascade = cv2.CascadeClassifier(
    'data/haarcascade_indian_number_plate.xml')

# while True:
img = car.copy()
# new_width = 320
# scale_factor = new_width / img.shape[1]
# new_height = scale_factor * img.shape[0]
# new_shape = (new_width, int(new_height))
# img = cv2.resize(img, new_shape)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
number_plates = number_plate_cascade.detectMultiScale(img_gray, 1.3, 5)
for (x, y, w, h) in number_plates:
    area = w * h
    if area > min_area:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cv2.putText(img, "Number Plate", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 255, 0), 2)
    image = img[y : y + h, x : x + w]
    cv2.imshow("Number Plate", image)

cv2.imshow("Result", img)
# if cv2.waitKey(0) & 0xFF == ord('q'):
#     cv2.destroyAllWindows()

if cv2.waitKey(0) & 0xFF == ord('s'):
    cv2.imwrite("data/scanned/numberplate.jpg", image)
    cv2.rectangle(img, (0, 50), (600, 200), (0, 255, 0), cv2.FILLED)
    cv2.putText(img, "Scanned successfully", (125, 125), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 2)
    cv2.imshow("Result", img)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()
