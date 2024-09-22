import cv2
import numpy as np
from ultralytics import YOLO
import face_recognition
from datetime import timedelta

model = YOLO('yolov8n-face.pt')

def load_yolo_model():
    """
    Load the YOLOv8 model for face detection.
    """
    # Assuming you have a pre-trained YOLOv8 model for face detection
    return YOLO('yolov8n-face.pt')


def detect_faces(model, frame):
    """
    Detect faces in a given frame using YOLOv8.
    """
    results = model(frame)
    return results[0].boxes.xyxy.cpu().numpy()


def compare_faces(known_face_encoding, face_encoding):
    """
    Compare detected face with the reference face.
    """
    return face_recognition.compare_faces([known_face_encoding], face_encoding)[0]


def process_video(video_path, reference_image_path, yolo_model):
    """
    Process the video to detect and match faces.
    """
    # Load the reference image
    reference_image = face_recognition.load_image_file(reference_image_path)
    reference_encoding = face_recognition.face_encodings(reference_image)[0]

    # Open the video file
    video = cv2.VideoCapture(video_path)
    fps = video.get(cv2.CAP_PROP_FPS)

    matches = []

    while True:
        ret, frame = video.read()
        if not ret:
            break

        # Get the current timestamp
        timestamp = video.get(cv2.CAP_PROP_POS_MSEC) / 1000.0

        # Detect faces using YOLOv8
        detections = detect_faces(yolo_model, frame)

        for detection in detections:
            x1, y1, x2, y2 = detection[:4].astype(int)
            face_image = frame[y1:y2, x1:x2]

            # Get face encoding
            face_encoding = face_recognition.face_encodings(face_image)

            if face_encoding:
                # Compare with reference face
                if compare_faces(reference_encoding, face_encoding[0]):
                    matches.append(timestamp)

    video.release()
    return matches


def main():
    video_path = 'path_to_your_video.mp4'
    reference_image_path = 'path_to_reference_image.jpg'

    yolo_model = load_yolo_model()

    matches = process_video(video_path, reference_image_path, yolo_model)

    for match in matches:
        time = str(timedelta(seconds=int(match))).split('.')[0]
        print(f"Match found at: {time}")


if __name__ == "__main__":
    main()