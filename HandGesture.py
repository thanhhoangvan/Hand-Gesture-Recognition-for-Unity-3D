import cv2


cam = cv2.VideoCapture(0)


while True:
    result, image = cam.read()
    
    cv2.imshow("hand Detection", image)

    k = cv2.waitKey(1)
    # ESC pressed -> quit
    if k%256 == 27:
        break

cv2.destroyWindow("GeeksForGeeks")
