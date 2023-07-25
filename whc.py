import cv2

cap = cv2.imread("C:\Users\the eye informatique\Desktop\internship\3.JPG") # this is to open webcam camera
while True: #infinite loop
    #ignore, frame = cap.read() # reads the image
    cv2.imshow("me", cap)
        # me is the name of the window.
        # frame is the matrix (image)
    #w,h,c = frame.shape #getting the width, height and channel (BGR)
    #print(w,h,c)
    key = cv2.waitKey(1) #returns the one parameter that has been read.
    if key == ord("q"):
        break
cap.release()
cv2.destroyAllWindows
