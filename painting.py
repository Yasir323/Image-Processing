import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Width
cap.set(4, 480)  # Height
# cap.set(10, 50) # Brightness

my_colors = [111, 93, 73, 149, 255, 255]
my_color_values = [207, 97, 58]
my_points = []  # [x, y, color_id]


def find_color(img, my_color_values):
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    new_points = []
    lower = np.array(my_colors[0:3])
    upper = np.array(my_colors[3:6])
    mask = cv2.inRange(img_hsv, lower, upper)
    x, y = get_contours(mask)
    cv2.circle(img_result, (x, y), 10, my_color_values, cv2.FILLED)
    # cv2.imshow("Img", mask)
    if x != 0 and y != 0:
        new_points.append([x, y])
    return new_points


def get_contours(img):
    contours, hierarchy = cv2.findContours(
        img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        # print(area)
        if area > 1000:
            # cv2.drawContours(img_result, cnt, -1, (0, 0, 0), 4)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.012 * peri, True)
            x, y, w, h = cv2.boundingRect(approx)
    return x + w // 2, y

def draw(my_points, my_color_values):
    for point in my_points:
        cv2.circle(img_result, (point[0], point[1]), 10, my_color_values, cv2.FILLED)



while True:
    success, img = cap.read()
    img_result = img.copy()
    new_points = find_color(img, my_color_values)
    if len(new_points) != 0:
        for new_point in new_points:
            my_points.append(new_point)

    if len(my_points) != 0:
        draw(my_points, my_color_values)
    cv2.imshow("Video", img_result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
