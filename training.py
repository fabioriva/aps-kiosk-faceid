import cv2
import csv
import numpy as np
import os
import sys

min_float = sys.float_info.min
print(f"The minimum float value in Python is: {min_float}")

max_float = sys.float_info.max
print(f"The maximum float value in Python is: {max_float}")


csv_file = "directory_structure.csv"

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer = cv2.face.LBPHFaceRecognizer_create(threshold=31.0)

threshold = recognizer.getThreshold()


def get_images_and_labels():
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        faces = []
        ids = []
        names = []
        for row in reader:
            image_path = row[0]
            id = row[1]
            # print(image_path, id, row[2])
            img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            faces.append(img)
            ids.append(int(id))
            names.append(row[2])
    return faces, ids, names


def model_info(model):
    print(f"Model name: {model.getDefaultName()}")
    print(f"Radius: {model.getRadius()}")
    print(f"Neighbours: {model.getNeighbors()}")
    print(f"Grid X: {model.getGridX()}")
    print(f"Grid Y: {model.getGridY()}")
    print(f"Threshold: {model.getThreshold()}")


def print_result(id, confidence, names):
    print(
        f"Result ID: {id}, Confidence: {confidence}, Person: {names[id] if id > 0 and id < len(names) else 'unknown'}")


faces, ids, names = get_images_and_labels()
# # print(faces[0], len(faces))
# # print(ids, len(ids), ids[0], type(ids[0]))
recognizer.train(faces, np.array(ids))
recognizer.save('trainer.yml')

model_info(recognizer)

# sample = faces[3]

# id, confidence = recognizer.predict(sample)
# print("\nSame")
# print_result(id, confidence, names)
# model_info(recognizer)

# recognizer.setThreshold(50.0)

# sample = cv2.imread("dataset/User.1.9.jpg", cv2.IMREAD_GRAYSCALE)
# id, confidence = recognizer.predict(sample)
# print("\nRaffaele")
# print_result(id, confidence, names)
# model_info(recognizer)

# sample = cv2.imread("dataset/User.2.22.jpg", cv2.IMREAD_GRAYSCALE)
# id, confidence = recognizer.predict(sample)
# print("\nFabio")
# print_result(id, confidence, names)
# model_info(recognizer)

for file_name in os.listdir('dataset'):
    print("img: " + file_name)
    img_path = os.path.join('dataset', file_name)
    sample = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    id, confidence = recognizer.predict(sample)
    if (confidence <= threshold):
        print_result(id, confidence, names)

# with open(csv_file, 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         image_path = row[0]
#         sample = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
#         id, confidence = recognizer.predict(sample)
#         if (confidence <= threshold):
#             print_result(id, confidence, names)

# # recognizer.setThreshold(0.0)
# # id, confidence = recognizer.predict(sample)
# # print("\nNull")
# # print_result(id, confidence, names)
# # model_info(recognizer)
