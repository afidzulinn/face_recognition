from ultralytics import YOLO

model = YOLO('model/yolov8n-face.pt')

print(model)