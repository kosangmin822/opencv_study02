import numpy as np
import cv2

img = cv2.imread('images/1.jpg', cv2.IMREAD_GRAYSCALE)

ret, thr1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret, thr2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
ret, thr3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
ret, thr4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
ret, thr5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

cv2.imshow('original', img)
cv2.imshow('Binary', thr1)
cv2.imshow('Binary_inv', thr2)
cv2.imshow('Trunc', thr3)
cv2.imshow('ToZero', thr4)
cv2.imshow('ToZero_inv', thr3)

cv2.waitKey(0)
cv2.destroyAllWindows()




