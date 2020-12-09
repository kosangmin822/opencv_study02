import cv2


def onMouse(x):
    pass


def addimage(imgfile1, imgfile2):
    img1 = cv2.imread(imgfile1)
    img2 = cv2.imread(imgfile2)

    cv2.namedWindow('ImgPane')
    cv2.createTrackbar('Mixing', 'ImgPane', 0, 100, onMouse)
    mix = cv2.getTrackbarPos('Mixing', 'ImgPane')

    while True:
        img = cv2.addWeighted(img1, float(100 - mix) / 100, img2, float(mix) / 100, 0)
        cv2.imshow('imgPane', img)

        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

        mix = cv2.getTrackbarPos('Mixing', 'ImgPane')

    cv2.destroyAllWindows()


addimage('images/1.jpg', 'images/2.jpg')
