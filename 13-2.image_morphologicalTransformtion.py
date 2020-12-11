import cv2
import numpy as np


def morph():
    img1 = cv2.imread('images/a.jpg', cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread('images/b.jpg', cv2.IMREAD_GRAYSCALE)

    kernel = np.ones((5, 5), np.uint8)

    opening = cv2.morphologyEx(img1, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(img2, cv2.MORPH_CLOSE, kernel)

    cv2.imshow('open', opening)
    cv2.imshow('close', closing)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


morph()
