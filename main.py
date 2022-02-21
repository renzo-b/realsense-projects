from scipy.misc import face

from face_tracking import *
from frame_manager import CaptureManager
from image_processors import *
from realsense_manager import RealsenseManager

# camera
camera = RealsenseManager(mode="rgbd")
camera.setup_pipeline()

# image processor
blur_processor = EdgeDetector(5, True)
face_tracker = FaceTracker(True)

capture_manager = CaptureManager()
capture_manager.set_camera(camera)
capture_manager.create_window()
capture_manager.set_analysis(face_tracker)
capture_manager.run()
