import cv2
import sys
import numpy as np;
from matplotlib import pyplot as plt

# 
# ------------ Main

cap = cv2.VideoCapture('tests/videos/1.mp4')
image = cv2.imread('tests/images/1.jpg', 1)

# if not cap.isOpened():
#     sys.exit(-2)

while True:
    # ret, image = cap.read()
    height, width, channels = image.shape

    crop_img = image[height*0.0:height, 0:width]

    gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY) # grayscale
    template = cv2.imread('tests/images/headSprites/mario/3.png', 0)

    w,h = template.shape[::-1]

    res = cv2.matchTemplate(gray, template, cv2.TM_CCORR_NORMED)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(crop_img,top_left, bottom_right, 255, 2)

    cv2.imshow('frame', crop_img)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()