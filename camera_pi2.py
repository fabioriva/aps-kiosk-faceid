import cv2
import csv
import time
from base_camera import BaseCamera
from picamera2 import Picamera2, Preview
from faceid_cv2 import face_capture, face_detection, face_recognition
# from faceid import analysis

"""
Parameters
radius	The radius used for building the Circular Local Binary Pattern. The greater the radius, the smoother the image but more spatial information you can get.
neighbors	The number of sample points to build a Circular Local Binary Pattern from. An appropriate value is to use 8 sample points. Keep in mind: the more sample points you include, the higher the computational cost.
grid_x	The number of cells in the horizontal direction, 8 is a common value used in publications. The more cells, the finer the grid, the higher the dimensionality of the resulting feature vector.
grid_y	The number of cells in the vertical direction, 8 is a common value used in publications. The more cells, the finer the grid, the higher the dimensionality of the resulting feature vector.
threshold	The threshold applied in the prediction. If the distance to the nearest neighbor is larger than the threshold, this method returns -1.
"""
RADIUS = 1
NEIGHBORS = 8
GRID_X = 8
GRID_Y = 8
THRESHOLD = 30.0

CSV = "directory_structure.csv"
# MODEL='trainer/model.yml'
MODEL = 'trainer.yml'


def get_names():
    with open(CSV, 'r') as file:
        reader = csv.reader(file)
        names = []
        for row in reader:
            names.append(row[2])
    # print(names, type(names), names[-1], type(names[-1]))
    return names


class Camera(BaseCamera):
    @ staticmethod
    def frames():
        with Picamera2() as camera:

            face_detector = cv2.CascadeClassifier(
                cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            face_recognizer = cv2.face.LBPHFaceRecognizer_create(
                radius=RADIUS, neighbors=NEIGHBORS, grid_x=GRID_X, grid_y=GRID_Y, threshold=THRESHOLD)
            face_recognizer.read(MODEL)

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
            names = get_names()

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
                        face_recognition(im, face_detector,
                                         face_recognizer, names)

                    # as a jpeg image and return it
                    yield cv2.imencode('.jpg', im)[1].tobytes()

            finally:
                camera.stop()
