import cv2
import sys
# 
# ------------ Main

cap = cv2.VideoCapture('tests/videos/2.mp4')

if not cap.isOpened():
    sys.exit(-2)

while True:
    ret, image = cap.read()
    height, width, channels = image.shape

    crop_img = image[height*0.75:height, 0:width]

    cv2.imshow('frame2', crop_img)

    gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY) # grayscale
    _, thresh = cv2.threshold(gray,10,255,cv2.THRESH_BINARY_INV) # threshold
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
    dilated = cv2.dilate(thresh,kernel,iterations = 13) # dilate
    imagemp, contours, hierarchy = cv2.findContours(dilated,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) # get contours
# for each contour found, draw a rectangle around it on original image
    for contour in contours:
    # get rectangle bounding contour
        [x,y,w,h] = cv2.boundingRect(contour)

    # discard areas that are too large
        if h>height*.5 or w>width*.5:
            continue

    # discard areas that are too small
        if h<height*.1 or w<width*.1:
            continue



    # draw rectangle around contour on original image
        cv2.rectangle(crop_img,(x,y),(x+w,y+h),(255,0,255),2)

    # write original image with added contours to disk
    cv2.imshow('frame', gray)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()