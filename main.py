from frame_manager import CaptureManager
from image_processors import *
from realsense_manager import RealsenseManager

# camera
camera = RealsenseManager(mode="rgbd")
camera.setup_pipeline()

# image processor
blur_processor = Blur((3, 3), True)

capture_manager = CaptureManager()
capture_manager.set_camera(camera)
capture_manager.create_window()
capture_manager.set_analysis(blur_processor)
capture_manager.run()
