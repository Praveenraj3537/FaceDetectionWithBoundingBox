import cv2
import mediapipe as mp

capture = cv2.VideoCapture(0)       # captures the video through webcam

faceDetect = mp.solutions.face_detection  #detecting the face using mediapipe lib
faceDraw = mp.solutions.drawing_utils
face = faceDetect.FaceDetection(0.5)
while True:
    sucess , image = capture.read()          #reading the video

    imgRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # converting to RGB
    result = face.process(imgRGB)
    if result.detections:
        for fa in result.detections:
            print(faceDetect.get_key_point(fa,faceDetect.FaceKeyPoint.RIGHT_EYE))  # as long as detection show face key point
            faceDraw.draw_detection(image,fa)


    cv2.imshow("Your FACE with BOX ", image)
    cv2.waitKey(27)