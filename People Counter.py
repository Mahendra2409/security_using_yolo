from ultralytics import YOLO
import cv2
import cvzone
import math
import time
import numpy as np

# cap = cv2.VideoCapture(0)  # For Webcam
# cap.set(3, 1280)
# cap.set(4, 720)
cap = cv2.VideoCapture("Videos/bikes.mp4")  # For Video


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
    success, img = cap.read()
    results = model(img, stream=True)

    # Reset the person count for this frame
    person_count = 0

    for r in results:
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
                cvzone.cornerRect(img, (x1, y1, w, h))

                # cvzone.cornerRect(img, (x1, y1, w, h), l=9, rt=5)
                cvzone.putTextRect(img, f'{currentClass} {conf}', (max(0, x1), max(35, y1)),
                                   scale=0.6, thickness=1, offset=3)
                # Increment the person count
                person_count += 1
                #currentArray = np.array([x1, y1, x2, y2, conf])
                #detections = np.vstack((detections, currentArray))

            #cvzone.putTextRect(img, f'{classNames[cls]} {conf}', (max(0, x1), max(35, y1)), scale=1, thickness=1)
    if person_count<=5:
        col=(255,0,0)
    elif person_count<=10:
        col=(0, 255 ,0)
    else:
        col=(0,0,255)


    # Display the number of people detected in the current frame
    cv2.putText(img, f'Person Count: {person_count}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (col), 2)
    #cv2.rectangle(img,(50,50),(200,200),col,-1)
    fps = 1 / (new_frame_time - prev_frame_time)
    prev_frame_time = new_frame_time
    print(fps)

    cv2.imshow("Image", img)
    cv2.waitKey(1)