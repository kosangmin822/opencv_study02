# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import cv2
import numpy as np
import matplotlib.pyplot as plt


def showImage():
    imgfile = 'images/1.jpg'
    img = cv2.imread(imgfile, cv2.IMREAD_COLOR)
    cv2.namedWindow('model', cv2.WINDOW_NORMAL)
    cv2.imshow('model', img)


    k = cv2.waitKey(0) & 0xFF
    if k == 27:
        cv2.destroyAllWindows()

    elif k == ord('c'):
        cv2.imwrite('images/model_copy.jpg', img)
        cv2.destroyAllWindows()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    showImage()
