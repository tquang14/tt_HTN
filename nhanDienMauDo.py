import  cv2
import numpy as np

cap = cv2.VideoCapture(0)
while 1:
    ret, image = cap.read()
    # convert the image to grayscale and blur to detect edges
    blurred_frame = cv2.GaussianBlur(image, (5, 5), 0)
    hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([0, 100, 100])
    upper_blue = np.array([10, 255, 250])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    contours = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    try:
        con = max(contours, key=cv2.contourArea)
        (circle_pos, radius) = cv2.minEnclosingCircle(con)
        if radius>5:
            print("mau do")
    except:
        pass
    cv2.imshow("mask",mask)
    cv2.imshow("frame",image)
    key = cv2.waitKey(1)
    if key == 27:
        break