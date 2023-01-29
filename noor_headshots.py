import cv2
import face_recognition
from picamera import PiCamera
from picamera.array import PiRGBArray
import time
import os

personName = 'test1' #replace with your name
parentDir = "/home/pi/facial-recognition-main/dataset/"
path = os.path.join(parentDir,personName)
os.mkdir(path)
cam = PiCamera()
cam.resolution = (640,480)#modified from 512, 304
cam.framerate = 20
rawCapture = PiRGBArray(cam, size=(640, 480))
    
img_counter = 0
timeout_start = time.time()
while True:
    for frame in cam.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        image = frame.array
        boxes = face_recognition.face_locations(image)
        detectedFaces = len(boxes)
        cv2.imshow("be in a frame ", image)
        rawCapture.truncate(0)
        
        k = cv2.waitKey(1)
        rawCapture.truncate(0)
        if detectedFaces == 1:
            img_name = "dataset/"+ personName +"/image_{}.jpg".format(img_counter)
            cv2.imwrite(img_name, image)
            print("{} written!".format(img_name))
            img_counter += 1
            
        elif detectedFaces>1:
            print("more than one person detected!!!")
        else:
            print("no faces detected!!! please come in frame")
        #time.sleep(0.20)
        if img_counter ==  65:
            print(time.time()-timeout_start)
            break
    if img_counter ==  65:
        break
    
cam.close()#modified
cv2.destroyAllWindows()
