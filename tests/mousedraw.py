import cv2
import numpy as np

# mouse callback function
def draw_circle(event, x, y, flags, param):
	if event == cv2.EVENT_LBUTTONDOWN:
		cv2.circle(img, (x,y),2,(255,0,0),-1)
		print "X: " + str(x) + " Y: " + str(y)

img = cv2.imread('stock.jpeg')
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
	cv2.imshow('image',img)
	if cv2.waitKey(20) & 0xff == 27:
		break
cv2.destroyAllWindows()