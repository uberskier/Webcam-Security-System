import cv2
import os
import numpy


cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

imgCount = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        print("Closing..")
        break
    elif k%256 == 32:
        imgName = "opencv_fram_{}.png".format(imgCount)
        path = '../Camera-Pictures'
        cv2.imwrite(os.path.join(path, imgName), frame)
        print("{} written!".format(imgName))
        imgCount += 1

cam.release()

cv2.destroyAllWindows()
