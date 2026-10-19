# OpenCV Computer Vision Projects

A collection of practical computer vision projects built using Python and OpenCV. This repository explores image processing, face detection, webcam-based detection, and human counting.

## Projects

### 1. Image Face Detection
- Detects faces in a static image.
- Uses OpenCV's Haar Cascade classifier.
- Draws bounding boxes and labels around detected faces.

### 2. Real-Time Webcam Face Detection
- Detects faces through a webcam in real time.
- Uses Haar Cascade face detection.
- Displays bounding boxes and detection labels.
- Press `q` to exit.

### 3. People Counter
- Detects people in webcam frames.
- Uses OpenCV's HOG descriptor and pretrained SVM people detector.
- Draws bounding boxes around detected people.
- Displays the current number of detected people.
- Press `q` to exit.

## Technologies Used

- Python
- OpenCV (`cv2`)
- Haar Cascade Classifier
- HOG (Histogram of Oriented Gradients)
- SVM (Support Vector Machine)

## Requirements

- Python 3
- OpenCV

Install OpenCV:

```bash
pip install opencv-python
```

## Project Structure

```text
opencv-computer-vision-projects/
├── FaceDetector/
│   ├── face_detector.py
│   ├── assets/
│   │   └── images/
│   │       └── murtaz.jpeg
│   └── PeopleCounter/
│       └── people_counter.py
└── README.md
```

*Note: Adjust the structure above if your actual folder layout differs.*

## How to Run

Run the face detection project:

```bash
python face_detector.py
```

Run the people counter:

```bash
python PeopleCounter/people_counter.py
```

Run commands from the appropriate directory, and ensure the image path in the face detection script points to the correct file.

## Learning Objectives

- Reading and displaying images with OpenCV
- Converting images to grayscale
- Detecting faces using Haar Cascades
- Processing live webcam frames
- Detecting human bodies using HOG and SVM
- Drawing bounding boxes and displaying text
- Building real-time computer vision applications

## Limitations

Detection accuracy depends on lighting, camera angle, distance, occlusion, and the detector being used. The people counter estimates the number of people detected in each frame; it does not track unique individuals across time.

## Future Improvements

- Improve detection accuracy.
- Add object detection using a modern pretrained model.
- Implement person tracking to avoid repeated counts across frames.

## Author

**Murtaz**

GitHub: [@murtaz-ai](https://github.com/murtaz-ai)

---

Built as part of my journey into computer vision and Artificial Intelligence.