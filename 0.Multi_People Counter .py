from ultralytics import YOLO
import cv2
import cvzone
import math
import time
import os
import torch
import numpy as np

# overlayList = []  # list to store all the images
# # images in header folder
# folderPath = "Header"
# myList = os.listdir(folderPath)  # getting all the images used in code
# for imPath in myList:  # reading all the images from the folder
#     image = cv2.imread(f'{folderPath}/{imPath}')
#     overlayList.append(image)  # inserting images one by one in the overlayList
# header = overlayList[0]  # storing 1st image

# Resize the image (width, height)
width = 1280  # Desired width
height = 720  # Desired height

# bg = cv2.imread('Header/1.png')

bg00 = cv2.resize(cv2.imread('Header/2/00.png'), (width, height))
bg01 = cv2.resize(cv2.imread('Header/2/01.png'), (width, height))
bg02 = cv2.resize(cv2.imread('Header/2/02.png'), (width, height))
bg10 = cv2.resize(cv2.imread('Header/2/10.png'), (width, height))
bg11 = cv2.resize(cv2.imread('Header/2/11.png'), (width, height))
bg12 = cv2.resize(cv2.imread('Header/2/12.png'), (width, height))
bg20 = cv2.resize(cv2.imread('Header/2/20.png'), (width, height))
bg21 = cv2.resize(cv2.imread('Header/2/21.png'), (width, height))
bg22 = cv2.resize(cv2.imread('Header/2/22.png'), (width, height))
bg=bg00


# For Webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# # For Additional
# cap1 = cv2.VideoCapture(1)
# cap1.set(3, 1280)
# cap1.set(4, 720)

# For Phone cam
cap2 = cv2.VideoCapture(1)
cap2.set(3, 1280)
cap2.set(4, 720)

# cap = cv2.VideoCapture("Videos/bikes.mp4")  # For Video


model = YOLO("Yolo-Weights/yolov8l.pt")

classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"
              ]
prev_frame_time = 0
new_frame_time = 0

while True:
    new_frame_time = time.time()
    success, img1 = cap.read()
    # success, img2 = cap1.read()
    success, img3 = cap2.read()

    results1 = model(img1, stream=True)
    # results2 = model(img2, stream=True)
    results3 = model(img3, stream=True)


    # Reset the person count for this frame
    person_count1 = 0
    person_count2 = 0
    person_count3 = 0


#1
    for r in results1:
        boxes = r.boxes
        for box in boxes:
            # Bounding Box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            # cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,255),3)
            w, h = x2 - x1, y2 - y1

            # Confidence
            conf = math.ceil((box.conf[0] * 100)) / 100

            # Class Name
            cls = int(box.cls[0])
            currentClass = classNames[cls]

            if currentClass == "person" and conf > 0.3:
                cvzone.cornerRect(img1, (x1, y1, w, h))

                # cvzone.cornerRect(img, (x1, y1, w, h), l=9, rt=5)
                cvzone.putTextRect(img1, f'{currentClass} {conf}', (max(0, x1), max(35, y1)),
                                   scale=0.6, thickness=1, offset=3)
                # Increment the person count
                person_count1 += 1
                #currentArray = np.array([x1, y1, x2, y2, conf])
                #detections = np.vstack((detections, currentArray))

            #cvzone.putTextRect(img, f'{classNames[cls]} {conf}', (max(0, x1), max(35, y1)), scale=1, thickness=1)
    if person_count1<=5:
        col=(255,0,0)
        # bg = bg00
        # header = overlayList[0]
    elif person_count1<=10:
        # bg = bg10
        col=(0, 255 ,0)
        # header = overlayList[1]
    else:
        # bg = bg20
        col=(0,0,255)
        # header = overlayList[2]
# #2
#     for r in results2:
#         boxes = r.boxes
#         for box in boxes:
#             # Bounding Box
#             x1, y1, x2, y2 = box.xyxy[0]
#             x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
#             # cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,255),3)
#             w, h = x2 - x1, y2 - y1
#
#             # Confidence
#             conf = math.ceil((box.conf[0] * 100)) / 100
#
#             # Class Name
#             cls = int(box.cls[0])
#             currentClass = classNames[cls]
#
#             if currentClass == "person" and conf > 0.3:
#                 cvzone.cornerRect(img2, (x1, y1, w, h))
#
#                 # cvzone.cornerRect(img, (x1, y1, w, h), l=9, rt=5)
#                 cvzone.putTextRect(img2, f'{currentClass} {conf}', (max(0, x1), max(35, y1)),
#                                    scale=0.6, thickness=1, offset=3)
#                 # Increment the person count
#                 person_count2 += 1
#                 #currentArray = np.array([x1, y1, x2, y2, conf])
#                 #detections = np.vstack((detections, currentArray))
#
#             #cvzone.putTextRect(img, f'{classNames[cls]} {conf}', (max(0, x1), max(35, y1)), scale=1, thickness=1)
#     if person_count2<=5:
#         col=(255,0,0)
#     elif person_count2<=10:
#         col=(0, 255 ,0)
#     else:
#         col=(0,0,255)
#3
    for r in results3:
        boxes = r.boxes
        for box in boxes:
            # Bounding Box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            # cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,255),3)
            w, h = x2 - x1, y2 - y1

            # Confidence
            conf = math.ceil((box.conf[0] * 100)) / 100

            # Class Name
            cls = int(box.cls[0])
            currentClass = classNames[cls]

            if currentClass == "person" and conf > 0.3:
                cvzone.cornerRect(img3, (x1, y1, w, h))

                # cvzone.cornerRect(img, (x1, y1, w, h), l=9, rt=5)
                cvzone.putTextRect(img3, f'{currentClass} {conf}', (max(0, x1), max(35, y1)),
                                   scale=0.6, thickness=1, offset=3)
                # Increment the person count
                person_count3 += 1
                #currentArray = np.array([x1, y1, x2, y2, conf])
                #detections = np.vstack((detections, currentArray))

            #cvzone.putTextRect(img, f'{classNames[cls]} {conf}', (max(0, x1), max(35, y1)), scale=1, thickness=1)
    if person_count3<=5:
        col=(255,0,0)
        # header = overlayList[0]
    elif person_count3<=10:
        col=(0, 255 ,0)
        # header = overlayList[1]
    else:
        col=(0,0,255)
        # header = overlayList[2]

    if person_count1<=5 and person_count3<=5 :
        bg = bg00
    elif person_count1<=5 and person_count3<=10 :
        bg = bg01
    elif person_count1<=5 and person_count3>10 :
        bg = bg02
    elif person_count1<=10 and person_count3<=5:
        bg = bg10
    elif person_count1 <= 10 and person_count3 <= 10:
        bg = bg11
    elif person_count1 <= 10 and person_count3 > 10:
        bg = bg12
    elif person_count1 > 10 and person_count3 <= 5:
        bg = bg20
    elif person_count1 > 10 and person_count3 <= 10:
        bg = bg21
    else :
        bg = bg22

    # else:
    #     # bg = bg20
    #     col=(0,0,255)
    #     # header = overlayList[2]


    # Display the number of people detected in the current frame
    cv2.putText(img1, f'Person Count: {person_count1}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (col), 2)
    # cv2.putText(img2, f'Person Count: {person_count2}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (col), 2)
    cv2.putText(img3, f'Person Count: {person_count3}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (col), 2)

    #cv2.rectangle(img,(50,50),(200,200),col,-1)
    fps = 1 / (new_frame_time - prev_frame_time)
    prev_frame_time = new_frame_time
#    print(fps)
    print("person_count1 :",person_count1,"person_count2 :",person_count2,"person_count3 :",person_count3)
    # img1 = header

    cv2.imshow("Image", img1)
    # cv2.imshow("Image2", img2)
    cv2.imshow("Image3", img3)
    # cv2.imshow("Output", bg)
    # Display the image
    cv2.imshow('Output', bg)

    cv2.waitKey(1) 