from ultralytics import YOLO
import cv2
import cvzone
import math
import time

# Constants
width, height = 1280, 720
bg_paths = [f'Header/2/{i}{j}.png' for i in range(3) for j in range(3)]
bgs = [cv2.resize(cv2.imread(path), (width, height)) for path in bg_paths]
classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat", "dog", "horse",
              "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella", "handbag", "tie",
              "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat", "baseball glove",
              "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup", "fork", "knife", "spoon",
              "bowl", "banana", "apple", "sandwich", "orange", "broccoli", "carrot", "hot dog", "pizza", "donut",
              "cake", "chair", "sofa", "pottedplant", "bed", "diningtable", "toilet", "tvmonitor", "laptop",
              "mouse", "remote", "keyboard", "cell phone", "microwave", "oven", "toaster", "sink", "refrigerator",
              "book", "clock", "vase", "scissors", "teddy bear", "hair drier", "toothbrush"]
cap1, cap2 = [cv2.VideoCapture(i) for i in range(2)]
for cap in [cap1, cap2]: cap.set(3, width), cap.set(4, height)

model = YOLO("Yolo-Weights/yolov8l.pt")

def detect_person(img, model):
    results = model(img, stream=True)
    count = 0
    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = box.conf[0]
            cls = int(box.cls[0])
            if classNames[cls] == "person" and conf > 0.3:
                count += 1
                w, h = x2 - x1, y2 - y1
                cvzone.cornerRect(img, (x1, y1, w, h))
                cvzone.putTextRect(img, f'person {conf:.2f}', (x1, y1 - 10), scale=0.6)
    return count

while True:
    success1, img1 = cap1.read()
    success2, img2 = cap2.read()
    if not (success1 and success2): break

    count1 = detect_person(img1, model)
    count2 = detect_person(img2, model)

    idx1 = 0 if count1 <= 5 else 1 if count1 <= 10 else 2
    idx2 = 0 if count2 <= 5 else 1 if count2 <= 10 else 2
    bg = bgs[idx1 * 3 + idx2]

    cv2.putText(bg, f'Counts: {count1}, {count2}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.imshow("Camera 1", img1)
    cv2.imshow("Camera 2", img2)
    cv2.imshow("Background", bg)

    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap1.release()
cap2.release()
cv2.destroyAllWindows()
