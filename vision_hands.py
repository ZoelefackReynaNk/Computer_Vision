import cv2
import mediapipe as mp
from datetime import datetime
import time


status_list=[None,None]
times=[]
cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
mpConnections = mp.solutions.hands_connections #getting from the libraries
hands = mpHands.Hands()#accesing the class in the library
mpDraw = mp.solutions.drawing_utils
pTime = 0
cTime = 0
while True:
    ignore, frame=cap.read()
    frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results = hands.process(frameRGB)
    status=0 
    #print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        print(results.multi_hand_landmarks)
        for handlms in results.multi_hand_landmarks:
            for id,lm in enumerate(handlms.landmark):
                
                h,w,c = frame.shape
                cx,cy = int(lm.x*w), int(lm.y*h)
                
                #print(h,w,c)
                if id == 8:
                    status=1
                    cv2.circle(frame,(cx,cy),25,(255,0,255),cv2.FILLED)
                    print(id,cx,cy)
                mpDraw.draw_landmarks(frame, handlms, mpConnections.HAND_CONNECTIONS)

            
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(frame,str("int(fps)"),(10,70),cv2.FONT_HERSHEY_COMPLEX,3,(255,0,255),3)
    cv2.imshow("frame",frame)
    key = cv2.waitKey(1)
    if key==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

