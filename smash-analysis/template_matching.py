import cv2
import sys
import numpy as np
from matplotlib import pyplot as plt

# 
# ------------ Main

cap = cv2.VideoCapture('../tests/videos/2.mp4')
image = cv2.imread('../tests/images/0.jpg', 1)

# if not cap.isOpened():
#     sys.exit(-2)

while True:
    ret, image = cap.read()
    height, width, channels = image.shape

    crop_img = image[height*0.75:height, 0:width]

    # gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY) # grayscale
    edges = cv2.Canny(crop_img, 100,200)

    cv2.imshow('edges', edges)

    template = cv2.imread('images/training/%.PNG', 0)

    w,h = template.shape[::-1]

    res = cv2.matchTemplate(edges, template, cv2.TM_CCORR_NORMED)

    threshold = 0.40
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(crop_img, pt, (pt[0] + w, pt[1] + h), 255, 2)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    # cv2.rectangle(crop_img,top_left, bottom_right, 255, 2)

    cv2.imshow('frame', crop_img)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()