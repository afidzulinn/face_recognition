This project detects faces in a video using YOLO and compares them with a reference image using FaceNet.

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Download the YOLO face detection model:
   ```
   wget https://github.com/derronqi/yolov8-face/releases/download/v0.0.0/yolov8n-face.pt
   ```

3. Place your video file and reference image in the project directory.

4. Update `video_path` and `reference_image_path` in `main.py`.

## Usage

Run the script:

```
python main.py
```

The script will output the timestamps where the reference face is found in the video.

## Documentation

- `detect_faces()`: Uses YOLO to detect faces in a frame.
- `get_face_embedding()`: Generates an embedding for a face image using FaceNet.
- `compare_faces()`: Compares two face embeddings.
- `process_video()`: Main function to process the video and find matching faces.
- `format_time()`: Converts seconds to HH:MM format.