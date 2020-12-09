import cv2


def showVideo():
    try:
        print('Camera On!')
        cap = cv2.VideoCapture(0)
    except:
        print('Camera Not Found!')
        return

    fps = 20.0
    width = int(cap.get(3))
    height = int(cap.get(4))
    fcc = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')
    out = cv2.VideoWriter('my_cam.avi', fcc, fps, (width, height))
    print('Starting Recoding')

    while True:
        ret, frame = cap.read()
        if not ret:
            print('Error Video Read')
            break

        cv2.imshow('viedo', frame)

        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            print('Stop to Recoding')
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()


showVideo()
