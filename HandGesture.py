import cv2
import time
import mediapipe as mp

pre_frame_time = 0
new_frame_time = 0
font = cv2.FONT_HERSHEY_SIMPLEX

cam = cv2.VideoCapture(0)

while True:
    sussess, image = cam.read()
    image = cv2.flip(image, 1)
    
    # Calculate FPS
    new_frame_time = time.time()
    FPS = 1/(new_frame_time - pre_frame_time)
    pre_frame_time = new_frame_time
    cv2.putText(image, "FPS: "+str(int(FPS)), (0, 40), font, 1, (100, 255, 0), 3, cv2.LINE_AA)

    cv2.imshow('Thanh HoangVan - Hand Gesture Recognition', image)
    k = cv2.waitKey(1)
    if k%256 == 27:
        break

cv2.destroyAllWindows()