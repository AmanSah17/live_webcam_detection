# YOLOv8 Live Object Detection

This repository contains a Python script for real-time object detection using the YOLOv8 model and a laptop's webcam. The script captures video from the webcam, performs object detection on each frame, and displays the results in a window.

## Features

- Real-time object detection using YOLOv8.
- Live video feed from the laptop's webcam.
- Press 'q' to exit the detection window.

## Requirements

- Python 3.7 or higher
- `opencv-python`
- `ultralytics`

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/yolov8-live-detection.git
cd yolov8-live-detection


2. Create a Virtual Environment
It is recommended to use a virtual environment to manage dependencies.

python3 -m venv yolov8-env
source yolov8-env/bin/activate  # On Windows use yolov8-env\Scripts\activate

2.1. Install the Required Packages
Install the necessary Python packages using pip:
pip install opencv-python ultralytics

2.2. Run the Script
Execute the script to start live object detection:
python live_detection.py



License
This project is licensed under the MIT License. See the LICENSE file for details.


### How to Use

1. **Clone the repository** to your local machine.
2. **Create a virtual environment** using the provided instructions.
3. **Install dependencies** with pip.
4. **Run the script** to start detecting objects in real-time using your laptop's webcam.
