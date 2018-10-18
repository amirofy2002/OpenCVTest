import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)


while(1):

    ret ,frame = cap.read()

    output = frame.copy()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    gray = cv.medianBlur(gray, 5)

    rows = gray.shape[0]

    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, rows / 8,
                              param1=100, param2=30,
                              minRadius=0, maxRadius=30)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            # circle center
            cv.circle(frame, center, 1, (0, 100, 100), 3)
            # circle outline
            radius = i[2]
            cv.circle(frame, center, radius, (255, 0, 255), 3)

    cv.imshow('img2', frame)

    k = cv.waitKey(60) & 0xff
    if k == 27:
        break