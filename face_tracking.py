import cv2
import numpy as np


class FaceTracker:
    """Tracks face"""

    def __init__(self, new_window):
        self.new_window = new_window

    def apply(self, image):
        face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        )
        scaling_factor = 0.8

        frame = cv2.resize(
            image,
            None,
            fx=scaling_factor,
            fy=scaling_factor,
            interpolation=cv2.INTER_AREA,
        )

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        face_rects = face_cascade.detectMultiScale(
            gray, scaleFactor=1.2, minNeighbors=5
        )

        for (x, y, w, h) in face_rects:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

        if self.new_window:
            cv2.imshow("Face Detector", frame)
