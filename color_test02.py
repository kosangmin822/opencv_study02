import numpy as np
import cv2


def tracking():
    try:
        print('Camera operation...')
        cap = cv2.VideoCapture(0)
    except:
        print('Camera is not operation')
        return

    while True:
        ret, frame = cap.read()

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_blue = np.array([90, 100, 100])
        upper_blue = np.array([150, 255, 255])

        lower_green = np.array([30, 100, 100])
        upper_green = np.array([90, 100, 100])

        lower_red = np.array([-30, 100, 100])
        upper_red = np.array([30, 100, 100])

        mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
        mask_green = cv2.inRange(hsv, lower_green, upper_green)
        mask_red = cv2.inRange(hsv, lower_red, upper_red)

        res1 = cv2.bitwise_and(frame, frame, mask=mask_blue)
        res2 = cv2.bitwise_and(frame, frame, mask=mask_green)
        res3 = cv2.bitwise_and(frame, frame, mask=mask_red)

        cv2.imshow('original', frame)
        cv2.imshow('blue', res1)
        cv2.imshow('green', res2)
        cv2.imshow('red', res3)

        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
    cv2.destroyAllWindows()


tracking()
