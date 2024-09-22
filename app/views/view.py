import cv2
from datetime import timedelta


class FaceDetectionView:
    @staticmethod
    def display_results(matches):
        for match in matches:
            time = str(timedelta(seconds=int(match))).split('.')[0]
            print(f"Match found at: {time}")

    @staticmethod
    def save_results(matches, output_file):
        with open(output_file, 'w') as f:
            for match in matches:
                time = str(timedelta(seconds=int(match))).split('.')[0]
                f.write(f"Match found at: {time}\n")