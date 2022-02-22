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
        # scaling_factor = 0.8

        # frame = cv2.resize(
        #     image,
        #     None,
        #     fx=scaling_factor,
        #     fy=scaling_factor,
        #     interpolation=cv2.INTER_AREA,
        # )

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        face_rects = face_cascade.detectMultiScale(gray, scaleFactor=2, minNeighbors=3)

        for (x, y, w, h) in face_rects:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)

        if self.new_window:
            cv2.imshow("Face Detector", image)

        return image, face_rects


def face_distance(depth, roi):
    for (x, y, w, h) in roi:
        distance_rect = depth[x : x + w, y : y + h]
        distance = distance_rect.mean()
        graphic_rect = cv2.rectangle(depth, (x, y), (x + w, y + h), (0, 255, 0), 3)

        cv2.rectangle(depth, (x, y), (x + w, y + h), (0, 255, 0), 3)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(
            depth, f"{distance}", (10, 450), font, 1, (0, 255, 0), 2, cv2.LINE_AA
        )

    cv2.imshow("depth_distance", depth)
