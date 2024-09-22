from app.controllers.controller import FaceDetectionController


def main():
    yolo_model_path = 'yolov8n-face.pt'
    video_path = 'path_to_your_video.mp4'
    reference_image_path = 'path_to_reference_image.jpg'
    output_file = 'results.txt'

    controller = FaceDetectionController(yolo_model_path)
    controller.run(video_path, reference_image_path, output_file)


if __name__ == "__main__":
    main()