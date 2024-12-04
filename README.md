# Metro Crowd Indicator

![Metro Crowd Indicator Demo](/Demo/Metro Coach Color change GIF.gif)

The **Metro Crowd Indicator** is an AI-powered application that uses YOLOv8 object detection to monitor and count the number of people in a metro coach in real time. This helps evaluate crowd density and provides a visual indication of occupancy levels, which can enhance passenger convenience and system efficiency.

## Features

- **Real-Time Detection**: Utilizes YOLOv8 to detect individuals in video feeds with high accuracy and speed.
- **Crowd Density Visualization**: Displays a bounding box and a label for each detected person on the video feed.
- **Dynamic Indicators**: Assigns colors based on crowd density:
  - **Blue**: Low occupancy (≤ 5 people)
  - **Green**: Moderate occupancy (6–10 people)
  - **Red**: High occupancy (> 10 people)
- **Multicoach Support**: Can handle video feeds from multiple cameras monitoring different coaches.

## Requirements

- Python 3.7 or higher
- The following Python libraries:
  - `ultralytics`
  - `cv2` (OpenCV)
  - `cvzone`
  - `torch`
  - `numpy`
  - `math`
  - `time`
  - `os`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/metro-crowd-indicator.git
   cd metro-crowd-indicator
2. Install the required Python libraries:
   ```bash
   pip install ultralytics opencv-python cvzone torch numpy
3. Download the YOLOv8 weights file (yolov8l.pt) and place it in the Yolo-Weights/ directory. You can download the weights from YOLOv8 GitHub repository.

## Usage

1. Ensure your webcam or other video input device is connected and accessible.
2. Run the script
   ```bash
   python metro_crowd_indicator.py
3. Use the q key to exit the application.

## Customization
- Adding More Coaches: Modify the for loop to dynamically add more camera inputs:
   ```bash
   for i in range(num_of_coaches):
    globals()[f"coach{i}"] = coach(camera_index)
Replace num_of_coaches with the desired number of camera feeds and camera_index with the respective indices for the video devices.
- Adjusting Detection Threshold: Update the confidence threshold in the classloop method:
   ```bash
   if currentClass == "person" and conf > 0.3:
Increase or decrease the 0.3 value to change the sensitivity.

##How It Works
1. **Video Capture:** The application reads video frames from the specified camera index using OpenCV.
2. **Object Detection:** YOLOv8 detects objects in the frames and filters detections to count only person objects.
3. **Crowd Analysis:**
	- Calculates the number of detected people.
	- Displays color-coded density indicators (blue, green, red) based on thresholds.
4. **Visualization:** Annotates the video feed with bounding boxes, class labels, and crowd density.







   
