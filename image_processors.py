import cv2
import numpy as np


class Blur:
    """Blurs images"""

    def __init__(self, kernel_size=(3, 3), new_window=None):
        self.kernel_size = kernel_size
        self.new_window = new_window

    def apply(self, image):
        kernel = np.ones(self.kernel_size, np.float32) / 9.0
        blurred = cv2.filter2D(image, -1, kernel)

        if self.new_window:
            cv2.imshow("Blurred Image", blurred)

        return blurred


class EdgeDetector:
    """Detects edge"""

    def __init__(self, threshold_1=30, threshold_2=100, new_window=None):
        self.threshold_1 = threshold_1
        self.threshold_2 = threshold_2
        self.new_window = new_window

    def apply(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        canny = cv2.Canny(gray, self.threshold_1, self.threshold_2)

        if self.new_window:
            cv2.imshow("Canny edges", canny)

        return canny


class GrayScale:
    """Converts image to gray"""

    def __init__(self, new_window=None):
        self.new_window = new_window

    def apply(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        if self.new_window:
            cv2.imshow("Gray", gray)

        return gray
