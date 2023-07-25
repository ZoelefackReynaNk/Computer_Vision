import cv2
import mediapipe as mp
import time
import math

mpPose = mp.solutions.pose
mpDraw = mp.solutions.drawing_utils
pose = mpPose.Pose()
cam = cv2.VideoCapture(0)
ptime=0
cord1=[0,0,0]
cord2=[0,0,0]
cord3=[0,0,0]

while True:
    ignore, frame = cam.read()
    frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results = pose.process(frameRGB)
    #print(results.pose_landmarks)
    if results.pose_landmarks:
        mpDraw.draw_landmarks(frame,results.pose_landmarks,mpPose.POSE_CONNECTIONS)
        for id , lm in enumerate(results.pose_landmarks.landmark):
            print(f'[{id},{lm}]')
            h,w,c = frame.shape
            cx,cy = int(lm.x*w), int(lm.y*h)
            #print(f'[{id},{cx},{cy}]')
            #print(h,w,c)
            if (id==0 or id==20 or id==19):
                if id == 0:
                    cord1[0]=id
                    cord1[1]=cx
                    cord1[2]=cy
                if id==20:
                    cord2[0]=id
                    cord2[1]=cx
                    cord2[2]=cy
                if id==19:
                    cord3[0]=id
                    cord3[1]=cx
                    cord3[2]=cy
            #print(f'cord1=[{cord1[0]},{cord1[1]},{cord1[2]}] cord2=[{cord2[0]},{cord2[1]},{cord2[2]}]')
            x_diff_right=cord1[1]-cord2[1]
            y_diff_right=cord1[2]-cord2[2]
            x_diff_left=cord1[1]-cord3[1]
            y_diff_left=cord1[2]-cord3[2]
            print(f'[{x_diff_left},{y_diff_left}] [{x_diff_right},{y_diff_right}')
            if (x_diff_left>=-100 and y_diff_left>=-50) or (x_diff_right<=100 and y_diff_right>=-50):
                cv2.putText(frame,str("hands on face"),(70,50),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,0),1)
    ctime = time.time()
    fps=1/(ctime-ptime)
    ptime=ctime
    #cv2.putText(frame, str(int(fps)),(70,50),cv2.FONT_HERSHEY_COMPLEX,3,(255,0,0),3)
    cv2.imshow("video",frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
print(h,w,c)
