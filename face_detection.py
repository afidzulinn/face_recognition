import cv2
import numpy as np
from ultralytics import YOLO
from deepface import DeepFace
import datetime

model = YOLO('model/yolov8n-face.pt')


def detect_and_compare_faces(video_path, reference_image_path):
    # Load the reference image
    reference_img = cv2.imread(reference_image_path)

    # Open the video file
    cap = cv2.VideoCapture(video_path)

    matches = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Get current timestamp
        timestamp = cap.get(cv2.CAP_PROP_POS_MSEC)

        # Detect faces using YOLO
        results = model(frame)

        for result in results:
            boxes = result.boxes.xyxy.cpu().numpy().astype(int)

            for box in boxes:
                x1, y1, x2, y2 = box
                face = frame[y1:y2, x1:x2]

                # Compare detected face with reference image
                try:
                    verification = DeepFace.verify(face, reference_img, enforce_detection=False)
                    if verification['verified']:
                        time = datetime.datetime.fromtimestamp(timestamp / 1000.0)
                        matches.append(time.strftime('%H:%M'))
                except:
                    pass

    cap.release()
    return matches


# Usage
video_path = 'path/to/your/video.mp4'
reference_image_path = 'path/to/your/reference_image.jpg'

matching_times = detect_and_compare_faces(video_path, reference_image_path)

print("Wajah yang cocok ditemukan pada waktu:")
for time in matching_times:
    print(time)