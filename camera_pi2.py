import time
from base_camera import BaseCamera
from picamera2 import Picamera2, Preview
from faceid import analysis


class Camera(BaseCamera):
    @staticmethod
    def frames():
        with Picamera2() as camera:

            camera_config = camera.create_preview_configuration({
                "format": "RGB888",
                "size": (480, 360)
            })
            camera.configure(camera_config)
            camera.start_preview(Preview.NULL)
            camera.start()

            # let camera warm up
            time.sleep(4)

            try:
                while True:
                    # deepface
                    yield from analysis(
                        camera=camera,
                        db_path="db",
                        enable_face_analysis=False,
                        model_name="VGG-Face")

                    # im = camera.capture_array()
                    # as a jpeg image and return it
                    # yield cv2.imencode('.jpg', im)[1].tobytes()

            finally:
                camera.stop()
