from ultralytics import YOLO
import cv2
import cvzone
import math
import time
import os
import torch
import numpy as np

#Model
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

# Resize the image (width, height)
width = 1280  # Desired width
height = 720  # Desired height

class coach :

    def __init__(self, cam_no):
        self.n = cam_no
        self.prev_frame_time = 0
        self.cap = cv2.VideoCapture(cam_no)
        self.cap.set(3, 1280)
        self.cap.set(4, 720)

    def classloop(self) :
        self.new_frame_time = time.time()
        success, self.img = self.cap.read()
        self.result = model(self.img, stream=True)
        self.person_count = 0

        for r in self.result:
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
                    cvzone.cornerRect(self.img, (x1, y1, w, h))

                    # cvzone.cornerRect(img, (x1, y1, w, h), l=9, rt=5)
                    cvzone.putTextRect(self.img, f'{currentClass} {conf}', (max(0, x1), max(35, y1)),
                                       scale=0.6, thickness=1, offset=3)
                    # Increment the person count
                    self.person_count += 1
                    # currentArray = np.array([x1, y1, x2, y2, conf])
                    # detections = np.vstack((detections, currentArray))

        if self.person_count <= 5:
            self.col = (255, 0, 0)
        elif self.person_count <= 10:
            self.col = (0, 255, 0)
        else:
            self.col = (0, 0, 255)

        self.fps = 1 / (self.new_frame_time - self.prev_frame_time)
        self.prev_frame_time = self.new_frame_time
        cv2.imshow(f'Image:{self.n}', self.img)

# coach = {}
# coach1 = coach(0)
# coach[2] = coach(1)

# Creating global variables dynamically
for i in range(1):
    globals()[f"coach{i}"] = coach(0)



while True :
    coach0.classloop()
    # coach[2].classloop()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
coach0.cap.release()
cv2.destroyAllWindows()