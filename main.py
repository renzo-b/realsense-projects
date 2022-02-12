import cv2
import numpy as np

from frame_manager import CaptureManager
from realsense_manager import RealsenseManager

camera = RealsenseManager()
camera.setup_pipeline()

capture_manager = CaptureManager()
capture_manager.create_window()

while capture_manager.window_open:

    depth_image, color_image = camera.capture_images()

    # Apply colormap on depth image (image must be converted to 8-bit per pixel first)
    depth_colormap = cv2.applyColorMap(
        cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET
    )

    frame = np.hstack((color_image, depth_colormap))

    capture_manager.get_frame(frame)
    capture_manager.show_frame()
    capture_manager.key_actions()
