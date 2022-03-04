import os
import cv2
import time

cap = cv2.VideoCapture(1)

while True:
    img, res = cap.read()
    cv2.imshow('Hand Gesture', img)

    cv2.waitKey(1)
    cv2.destroyAllWindows()
