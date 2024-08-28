import cv2
from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO("yolov8n.pt")  # Use yolov8n.pt for YOLOv8 nano, or replace with your model

# Open the webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture image.")
        break

    # Perform detection
    results = model(frame)

    # Draw the detection results on the frame
    annotated_frame = results[0].plot()

    # Display the resulting frame
    cv2.imshow('YOLOv8 Live Detection', annotated_frame)

    # Press 'q' to quit the webcam stream
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture and close windows
cap.release()
cv2.destroyAllWindows()
