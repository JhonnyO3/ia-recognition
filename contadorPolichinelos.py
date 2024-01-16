
import cv2
import mediapipe as mp
import math

video = cv2.VideoCapture('polichinelos.mp4')

pose = mp.solutions.pose
Pose = pose.Pose(min_tracking_confidence=0.5, min_detection_confidence=0.5)
draw = mp.solutions.drawing_utils
cont= 0
check = True


while True:
    success, img = video.read()
    videoRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = Pose.process(videoRGB)
    points = results.pose_landmarks
    draw.draw_landmarks(img, points, pose.POSE_CONNECTIONS)
    h, w, _ = img.shape
    
    
    if points:
        rightFootY = int(points.landmark[pose.PoseLandmark.RIGHT_FOOT_INDEX].y*h)
        rightFootX = int(points.landmark[pose.PoseLandmark.RIGHT_FOOT_INDEX].x*w)
        
        leftFootY = int(points.landmark[pose.PoseLandmark.LEFT_FOOT_INDEX].y*h)
        leftFootX = int(points.landmark[pose.PoseLandmark.LEFT_FOOT_INDEX].x*w)
        
        leftHandsY = int(points.landmark[pose.PoseLandmark.LEFT_INDEX].y*h)
        leftHandsX = int(points.landmark[pose.PoseLandmark.LEFT_INDEX].x*w)
        
        rightHandsY = int(points.landmark[pose.PoseLandmark.RIGHT_INDEX].y*h)
        rightHandsX = int(points.landmark[pose.PoseLandmark.RIGHT_INDEX].x*w)
        
        distHands = math.hypot(rightHandsX - leftHandsX, rightHandsX - leftHandsX )
        distFoot = math.hypot(rightFootX -leftFootX, rightFootY - leftFootY)
        
        if check == True and distHands <= 150 and distFoot >= 150:
            cont+=1
            check = False
        if distHands > 150 and distFoot < 150:
            check = True
  
        texto = f'QUANTIDADE {cont}'
        cv2.putText(img, texto, (40, 200), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,0,0), 5)
            
        
        
    
    cv2.imshow('Resultado', img)
    cv2.waitKey(40)