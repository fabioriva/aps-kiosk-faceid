import cv2
import time
from base_camera import BaseCamera
from picamera2 import Picamera2, Preview
from faceid_cv2 import face_capture, face_detection, face_recognition
# from faceid import analysis


class Camera(BaseCamera):
    @staticmethod
    def frames():
        with Picamera2() as camera:

            face_detector = cv2.CascadeClassifier(
                cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            face_recognizer = cv2.face.LBPHFaceRecognizer_create(
                # radius=1, neighbors=12, grid_x=8, grid_y=8, threshold=100)
                radius=2, neighbors=12, grid_x=8, grid_y=8, threshold=100)
            face_recognizer.read('trainer/model.yml')

            camera_config = camera.create_preview_configuration({
                "format": "RGB888",
                "size": (800, 1280)
            })
            camera.configure(camera_config)
            camera.start_preview(Preview.NULL)
            camera.start()

            # let camera warm up
            time.sleep(1)
            # init frame counter
            count = [0]

            try:
                while True:
                    # deepface
                    # yield from analysis(
                    #     camera=camera,
                    #     db_path="db",
                    #     enable_face_analysis=False,
                    #     model_name="VGG-Face")

                    im = camera.capture_array()

                    if (BaseCamera.mode == 'capture'):
                        face_capture(im, face_detector, count)
                    elif (BaseCamera.mode == 'detection'):
                        face_detection(im, face_detector)
                    elif (BaseCamera.mode == 'recognition'):
                        face_recognition(im, face_detector, face_recognizer)

                    # as a jpeg image and return it
                    yield cv2.imencode('.jpg', im)[1].tobytes()

            finally:
                camera.stop()
