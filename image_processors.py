import cv2
import numpy as np


class Blur:
    """Blurs images"""

    def __init__(self, kernel_size=(3, 3), new_window=None):
        self.kernel_size = kernel_size
        self.new_window = new_window

    def apply(self, image):
        kernel = np.ones(self.kernel_size, np.float32) / 9.0
        output = cv2.filter2D(image, -1, kernel)

        if self.new_window:
            cv2.imshow("Blurred Image", output)
