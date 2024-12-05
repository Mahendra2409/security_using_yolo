# Metro Crowd Indicator

![Metro Crowd Indicator](Demo/Metro_Coach_Color_change_GIF.gif)

**What if we know crowd status of each coach of upcoming metro in advance?**

- This Metro Crowd Indicator will be able to show Crowd level of each coach of upcoming metro at metro stations.
- So that people know where they should wait for less crowded coaches or Skip for next upcoming Metro.
- It update crowd status at every Station.

**What about Security at metros and metro Stations?**
- I also added security features.
- It can detect harmull objects like:`Gun`🔫,`Knife`🔪, `Fire`🔥 
- Dangerous Action: `Fighting`🤼, `Fallout`🧎
- And Send **ALERT** Message to Metro Security department.
- **⚠️ALERT MESSAGE** : It contains what found on CCTV footage and that clip🎥 in wchich it was found.

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
  - For GPU Acceleration Install Pytorch wchich is Compatible with your CUDA Version from [Pytorch Official Website](https://pytorch.org/get-started/locally/)
  ```bash
    pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
  
## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/metro-crowd-indicator.git
   cd metro-crowd-indicator
2. Install the required Python libraries:
   ```bash
   pip install ultralytics opencv-python cvzone numpy
3. Download the YOLOv8 weights file (yolov8l.pt) and place it in the Yolo-Weights/ directory. You can download the weights from YOLOv8 GitHub repository.


4. For GPU Acceleration Install Pytorch wchich is Compatible with your CUDA Version from [Pytorch Official Website](https://pytorch.org/get-started/locally/)
    ```bash
    pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
  
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







   
