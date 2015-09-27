import numpy as np
import sys
import cv2

def print_coords(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print 'x: ' + str(x) + ' y: ' + str(y)

cap = cv2.VideoCapture('tests/videos/1.mp4')
if not cap.isOpened():
    sys.exit(-1)

ret, frame = cap.read()
c,r,w,h = 175, 55, 25, 75
track_window = (c,r,w,h)

roi = frame[r:r+h, c:c+w]
hsv_roi =  cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_roi, np.array((0., 60.,32.)), np.array((180.,255.,255.)))
roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])
cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)

term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 20, 1 )

while cap.isOpened():
    ret, frame = cap.read()

    if ret == True:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)

        # apply meanshift to get the new location
        ret, track_window = cv2.CamShift(dst, track_window, term_crit)

        # Draw it on image
        pts = cv2.boxPoints(ret)
        pts = np.int0(pts)
        img2 = cv2.polylines(frame,[pts],True, 255,2)
        cv2.imshow('img2',img2)

        k = cv2.waitKey(20) & 0xff
        if k == 27:
            break
        else:
            cv2.imwrite(chr(k)+".jpg",img2)

    else:
        break
    #
    # cv2.imshow('frame',frame)
    # cv2.setMouseCallback('frame', print_coords)
    #
    # if cv2.waitKey(0) & 0xFF == ord('q'):
    #     break

cap.release()
cv2.destroyAllWindows()