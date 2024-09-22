import cv2
import numpy as np
from ultralytics import YOLO
import face_recognition


class FaceDetectionModel:
    def __init__(self, yolo_model_path):
        self.yolo_model = YOLO(yolo_model_path)

    def detect_faces(self, frame):
        results = self.yolo_model(frame)
        return results[0].boxes.xyxy.cpu().numpy()

    @staticmethod
    def compare_faces(known_face_encoding, face_encoding):
        return face_recognition.compare_faces([known_face_encoding], face_encoding)[0]

    @staticmethod
    def get_face_encoding(face_image):
        return face_recognition.face_encodings(face_image)