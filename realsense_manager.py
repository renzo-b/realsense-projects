from multiprocessing.sharedctypes import Value

import cv2
import numpy as np
import pyrealsense2 as rs


class RealsenseManager:
    def __init__(self, mode):
        """
        Manager for the RealSense camera

        Inputs
        ------
        mode: str
            mode to run the camera "rgb", "depth", or "rgbd"
        """
        self.pipeline = None
        self.config = None
        self.mode = mode

    def setup_pipeline(self):
        self.pipeline = rs.pipeline()
        self.config = rs.config()

        self.config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
        self.config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

        # Start streaming
        self.pipeline.start(self.config)

    def capture_images(self):
        """Gets image from the camera based on mode of operation"""
        frames = self.pipeline.wait_for_frames()

        if (self.mode == "rgb") or (self.mode == "rgbd"):
            color_frame = frames.get_color_frame()
            image = np.asanyarray(color_frame.get_data())
        if (self.mode == "depth") or (self.mode == "rgbd"):
            depth_frame = frames.get_depth_frame()
            depth_image = np.asanyarray(depth_frame.get_data())
            depth_colormap = cv2.applyColorMap(
                cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET
            )
            if self.mode == "depth":
                image = depth_colormap
            else:
                image = np.hstack((image, depth_colormap))

        return image
