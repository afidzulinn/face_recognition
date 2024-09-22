import cv2
import face_recognition

from app.models.model import FaceDetectionModel
from app.views.view import FaceDetectionView


class FaceDetectionController:
    def __init__(self, yolo_model_path):
        self.model = FaceDetectionModel(yolo_model_path)
        self.view = FaceDetectionView()

    def process_video(self, video_path, reference_image_path):
        reference_image = face_recognition.load_image_file(reference_image_path)
        reference_encoding = face_recognition.face_encodings(reference_image)[0]

        video = cv2.VideoCapture(video_path)
        fps = video.get(cv2.CAP_PROP_FPS)

        matches = []

        while True:
            ret, frame = video.read()
            if not ret:
                break

            timestamp = video.get(cv2.CAP_PROP_POS_MSEC) / 1000.0

            detections = self.model.detect_faces(frame)

            for detection in detections:
                x1, y1, x2, y2 = detection[:4].astype(int)
                face_image = frame[y1:y2, x1:x2]

                face_encoding = self.model.get_face_encoding(face_image)

                if face_encoding:
                    if self.model.compare_faces(reference_encoding, face_encoding[0]):
                        matches.append(timestamp)

        video.release()
        return matches

    def run(self, video_path, reference_image_path, output_file):
        matches = self.process_video(video_path, reference_image_path)
        self.view.display_results(matches)
        self.view.save_results(matches, output_file)