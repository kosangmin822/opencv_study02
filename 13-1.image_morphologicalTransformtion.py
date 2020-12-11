import cv2
import numpy as np


def morph():
    img = cv2.imread('images/abcd.jpg', cv2.IMREAD_GRAYSCALE)

    kernel = np.ones((3, 3), np.uint8)

    erosion = cv2.erode(img, kernel, iterations=3)
    dilation = cv2.dilate(img, kernel, iterations=3)

    cv2.imshow('original', img)
    cv2.imshow('erosion', erosion)
    cv2.imshow('dilation', dilation)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


morph()
