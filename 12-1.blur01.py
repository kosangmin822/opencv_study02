import cv2
import numpy as np


def bluring():
    img = cv2.imread('images/2.jpg')

    kernel = np.ones((100, 100), np.float32) / 10000
    blur = cv2.filter2D(img, -1, kernel)

    cv2.imshow('original', img)
    cv2.imshow('blur', blur)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


bluring()
