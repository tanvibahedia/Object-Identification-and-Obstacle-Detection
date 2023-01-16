import cv2
import time
import pyttsx3

cap = cv2.VideoCapture(0)   #VIDEO CAPTURE OBJECT DEFINATION
cap.set(3,640)
cap.set(4,480)

engine = pyttsx3.init()

classNames = []               #ARRAY DEFINED FOR DATABASE
classFile = 'coco.names'
with open(classFile,'rt') as x:
    classNames = x.read().rstrip('\n').split('\n')      #STORING NAMES IN ARRAY FROM COCO FILE
    configpath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
    weightspath = 'frozen_inference_graph.pb'

    net = cv2.dnn_DetectionModel(weightspath,configpath)
    net.setInputSize(320,320)
    net.setInputScale(1.0/ 127.5)
    net.setInputMean(127.5)
    net.setInputSwapRB(True)

while True:
    success, img = cap.read()
    classIDs, confs, bbox = net.detect(img,confThreshold = 0.5)
    print(classIDs,bbox)

    if len(classIDs) != 0:
        for classIDs, confidence, box in zip(classIDs.flatten(),confs.flatten(),bbox):      #GREEN BOX
            cv2.rectangle(img,box,color=(0,255,0),thickness=2)
            cv2.putText(img,classNames[classIDs-1].upper(),(box[0]+10, box[1]+30),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Output", img)       #DISPLAYING IMAGE
    engine.say(classNames[classIDs-1])      #AUDIO OUTPUT OF OBJECT DETECTED
    engine.runAndWait()
    cv2.waitKey(1)    #RUNS INFINITELY UNTIL KEY PRESSED
    time.sleep(2)