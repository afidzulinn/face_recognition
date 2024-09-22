# YOLOv8 Face Detection and Matching Project

## English

### Description
This project implements a face detection and matching system using YOLOv8. It processes a video file, detects faces, and matches them against a reference image. The system reports the timestamps where matching faces are found.

### Requirements
- Python 3.7+
- OpenCV
- Ultralytics YOLOv8
- face_recognition

### Installation
1. Clone this repository:
   ```
   git clone https://github.com/yourusername/yolov8-face-detection.git
   cd yolov8-face-detection
   ```

2. Install the required packages:
   ```
   pip install ultralytics opencv-python face_recognition
   ```

3. Download the YOLOv8 face detection model (e.g., 'yolov8n-face.pt') and place it in the project directory.

### Usage
1. Place your input video and reference image in the project directory.

2. Update the file paths in `main.py`:
   ```python
   yolo_model_path = 'yolov8n-face.pt'
   video_path = 'path_to_your_video.mp4'
   reference_image_path = 'path_to_reference_image.jpg'
   output_file = 'results.txt'
   ```

3. Run the main script:
   ```
   python main.py
   ```

4. The results will be displayed in the console and saved to `results.txt`.

### Project Structure
- `model.py`: Contains the FaceDetectionModel class for face detection and matching logic.
- `view.py`: Handles the display and saving of results.
- `controller.py`: Coordinates the interaction between the Model and View.
- `main.py`: Entry point of the application.

### License
[Specify your license here]

---

## Bahasa Indonesia

### Deskripsi
Proyek ini mengimplementasikan sistem deteksi dan pencocokan wajah menggunakan YOLOv8. Sistem ini memproses file video, mendeteksi wajah, dan mencocokkannya dengan gambar referensi. Sistem melaporkan timestamp di mana wajah yang cocok ditemukan.

### Persyaratan
- Python 3.7+
- OpenCV
- Ultralytics YOLOv8
- face_recognition

### Instalasi
1. Klon repositori ini:
   ```
   git clone https://github.com/namapengguna/yolov8-face-detection.git
   cd yolov8-face-detection
   ```

2. Instal paket yang diperlukan:
   ```
   pip install ultralytics opencv-python face_recognition
   ```

3. Unduh model deteksi wajah YOLOv8 (misalnya, 'yolov8n-face.pt') dan tempatkan di direktori proyek.

### Penggunaan
1. Tempatkan video input dan gambar referensi Anda di direktori proyek.

2. Perbarui path file di `main.py`:
   ```python
   yolo_model_path = 'yolov8n-face.pt'
   video_path = 'path_ke_video_anda.mp4'
   reference_image_path = 'path_ke_gambar_referensi.jpg'
   output_file = 'hasil.txt'
   ```

3. Jalankan script utama:
   ```
   python main.py
   ```

4. Hasil akan ditampilkan di konsol dan disimpan ke `hasil.txt`.

### Struktur Proyek
- `model.py`: Berisi kelas FaceDetectionModel untuk logika deteksi dan pencocokan wajah.
- `view.py`: Menangani tampilan dan penyimpanan hasil.
- `controller.py`: Mengkoordinasikan interaksi antara Model dan View.
- `main.py`: Titik masuk aplikasi.

### Lisensi
[Tentukan lisensi Anda di sini]
