import cv2 as cv
img = cv.imread('reyna.jpg')
cv.imshow('Me', img)

#converting an image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#bluring an image
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow('bluered image', blur)

#edge Cascade 
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# dilating images
dilated = cv.dilate(canny, (7, 7), iterations=3)
cv.imshow('dialted', dilated)

#eroded 
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('eroded', eroded)

#resize and crop an image
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow('resized', resized)

#cropping
cropped = img[50:200, 200:400]
cv.imshow('cropped', cropped)

cv.waitKey(0)