import sys
import cv2
import numpy as np

im = cv2.imread("tests/images/2.jpg", cv2.IMREAD_ANYCOLOR)


keypoints = detector.detect(im)

im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)