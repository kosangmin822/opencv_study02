import numpy as np
import cv2
import matplotlib.pyplot as plt


def canny():
    img = cv2.imread('images/3.jpg', cv2.IMREAD_GRAYSCALE)

    edge1 = cv2.Canny(img, 20, 200)
    edge2 = cv2.Canny(img, 100, 200)
    edge3 = cv2.Canny(img, 170, 200)

    cv2.imshow('original', img)
    cv2.imshow('50', edge1)
    cv2.imshow('100', edge2)
    cv2.imshow('170', edge3)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


canny()
