import numpy as np
import sys
import cv2
import tesseract as te

cap = cv2.VideoCapture('tests/videos/1.mp4')

if not cap.isOpened():
    sys.exit(-1)

while cap.isOpened():
    ret, frame = cap.read()

cap.release()
cv2.destroyAllWindows()