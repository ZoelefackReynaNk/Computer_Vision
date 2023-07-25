import cv2
import numpy as np

cap = cv2.VideoCapture(0) # this is to open webcam camera
while True: #infinite l
    
    ignore, frame = cap.read() # reads the image
    hsv = cv2.convert.color(frame, cv2, COLOR_BGR2HLS)
    high_blue = np.array([198, 215, 255]) # different colours have different BGR values
    low_blue = np.array([38, 86, 0])
    mask = cv2.inRange(hsv, low_blue, high_blue)
       #cv2.imshow("me", frame)
    #cv2.imshow("me", hsv)
    #cv2.imshow("me mask", mask)
        # me is the name of the window.
        # frame is the matrix (image)
    contours,_ = cv2.findContours(mask, cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    contours = sorted(contours, key = lambda x:cv2.contourArea(x), reverse = True)
    for cnts in contours: 
        (x,w,a,b) = cv2.boundingRect(cnts)
        cv2.rectangle(frame, (x,w), (x+a,w+b), (0,255,0), 3)
        break
   
    key = cv2.waitKey(1) #returns the one parameter that has been read.
    if key == ord("q"):
        break
    cap.release()
    cv2.destroyAllWindows
