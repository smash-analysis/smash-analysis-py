import cv2
import sys
import numpy as np
from matplotlib import pyplot as plt

# 
# ------------ Main

cap = cv2.VideoCapture('tests/videos/2.mp4')
image = cv2.imread('tests/images/2.jpg', 1)

# if not cap.isOpened():
#     sys.exit(-2)

while True:
    ret, image = cap.read()

    edges = cv2.Canny(image, 100,200)


    cv2.imshow('frame', edges)

    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()