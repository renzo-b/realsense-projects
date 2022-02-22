from scipy.misc import face

from face_tracking import *
from frame_manager import CaptureManager
from image_processors import *
from realsense_manager import RealsenseManager
from utils import split_image

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


def run_custom():
    while capture_manager.window_open:
        image = capture_manager.camera.capture_images()
        rgb, depth = split_image(image)

        rgb_with_rect, rect = face_tracker.apply(rgb)
        face_distance(depth, rect)

        cv2.imshow("rgb", rgb)
        cv2.imshow("depth", depth)

        capture_manager.key_actions()


capture_manager.run = run_custom
capture_manager.run()
