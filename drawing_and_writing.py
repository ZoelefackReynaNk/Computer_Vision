import cv2 as cv
import numpy as np

#create a blank image
blank = np.zeros((500,500, 3), dtype='uint8')
# paint image a certain color
blank[:] = 255, 0, 0
cv.imshow('blank', blank)
# img = cv.imread('prosper.jpg')
# cv.imshow('Prosper', img)

# draw a rectangle
cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=2)
cv.imshow('rectangle', blank)

#draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=3)
cv.imshow('circle', blank)

# draw a line 
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255, 255, 255), thickness=3)
cv.imshow('line', blank)

# write text on image.
cv.putText(blank, 'Hello', (225,25), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), thickness=2)
cv.imshow('text', blank)
cv.waitKey(0)