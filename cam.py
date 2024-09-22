import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk
import cv2
from ultralytics import YOLO

# Muat model YOLOv8 untuk deteksi wajah
model = YOLO('model/yolov8n-face.pt')

class FaceDetectionApp:
    def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source

        # Open video source (default is the webcam)
        self.vid = cv2.VideoCapture(self.video_source)

        # Create a canvas that can fit the video source size
        self.canvas = tk.Canvas(window, width=self.vid.get(cv2.CAP_PROP_FRAME_WIDTH),
                                height=self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.canvas.pack()

        # Button to close the application
        self.btn_quit = tk.Button(window, text="Quit", command=self.quit)
        self.btn_quit.pack()

        # Start the video loop
        self.update()

        self.window.mainloop()

    def update(self):
        # Get a frame from the video source
        ret, frame = self.vid.read()

        if ret:
            # Apply YOLO face detection to the frame
            results = model(frame)

            # Draw bounding boxes around detected faces
            for result in results:
                for bbox in result.boxes:
                    x1, y1, x2, y2 = map(int, bbox.xyxy[0])
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

            # Convert the image to PIL format
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)

            # Update image on canvas
            self.canvas.create_image(0, 0, anchor=tk.NW, image=imgtk)
            self.canvas.imgtk = imgtk

        # Repeat every 10 ms
        self.window.after(10, self.update)

    def quit(self):
        self.vid.release()
        self.window.quit()

# Create a window and pass it to the FaceDetectionApp class
window = tk.Tk()
FaceDetectionApp(window, "YOLOv8 Face Detection")