import cv2
import numpy


class CaptureManager:
    def __init__(self):
        self.window_name = "capture"
        self.frame = None
        self.window_open = False

    def create_window(self):
        cv2.namedWindow(self.window_name, cv2.WINDOW_AUTOSIZE)
        self.window_open = True

    def destroy_window(self):
        cv2.destroyWindow(self.window_name)
        self.window_open = False

    def key_actions(self):
        key_pressed = cv2.waitKey(1)

        if key_pressed == ord("q"):
            self.destroy_window()
        elif key_pressed == ord("s"):
            self.save_frame()

    def get_frame(self, frame):
        self.frame = frame

    def show_frame(self):
        cv2.imshow(self.window_name, self.frame)

    def save_frame(self):
        cv2.imwrite("frame.png", self.frame)

