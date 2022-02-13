import cv2
import numpy as np

from image_processors import Blur


class CaptureManager:
    def __init__(self):
        self.window_name = "capture"
        self.frame = None
        self.window_open = False
        self.camera = None
        self.analysis = None

    def run(self):
        while self.window_open:
            image = self.camera.capture_images()

            if self.analysis:
                self.analysis.apply(image)

            self.set_frame(image)
            self.show_frame()
            self.key_actions()

    def create_window(self):
        cv2.namedWindow(self.window_name, cv2.WINDOW_AUTOSIZE)
        self.window_open = True

    def destroy_windows(self):
        cv2.destroyAllWindows()
        self.window_open = False

    def key_actions(self):
        key_pressed = cv2.waitKey(1)

        if key_pressed == ord("q"):
            self.destroy_windows()
        elif key_pressed == ord("s"):
            self.save_frame()

    def set_frame(self, frame):
        self.frame = frame

    def show_frame(self):
        cv2.imshow(self.window_name, self.frame)

    def save_frame(self):
        cv2.imwrite("frame.png", self.frame)

    def set_camera(self, camera):
        self.camera = camera

    def set_analysis(self, analysis):
        self.analysis = analysis
