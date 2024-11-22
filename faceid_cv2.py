import cv2
import os

COLOR = (255, 0, 0)  # blue
YELLOW = (0, 255, 255)  # yellow
FONT = cv2.FONT_HERSHEY_COMPLEX
HEIGHT = 1
THICKNESS = 2

COUNT_LIMIT = 30
# NAMES = ['None', 'Raffaele Valli', 'Fabio Riva']


def face_capture(im, face_detector, count):
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    # Create a DS faces- array with 4 elements- x,y coordinates top-left corner), width and height
    faces = face_detector.detectMultiScale(gray, 1.1, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(im, (x, y), (x + w, y + h),
                      COLOR, THICKNESS)
        if (count[0] < COUNT_LIMIT):
            cv2.putText(im, 'Count: ' + str(int(count[0])), (x+5, y-5),
                        FONT, HEIGHT, COLOR, THICKNESS)
            count[0] += 1  # increment count

            # if dataset folder doesnt exist create:
            # if not os.path.exists("data"):
            os.makedirs("data", exist_ok=True)
            os.makedirs("data/s1", exist_ok=True)
            # .pgm portable gray map
            filePath = os.path.join("data/s1", f"{count[0]}.jpg")
            cv2.imwrite(filePath, gray[y:y+h, x:x+w])

        else:
            cv2.putText(im, 'Done: ' + str(int(count[0])), (x+5, y-5),
                        FONT, HEIGHT, COLOR, THICKNESS)


def face_detection(im, face_detector):
    # Convert fram from BGR to grayscale
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    # Create a DS faces- array with 4 elements- x,y coordinates top-left corner), width and height
    faces = face_detector.detectMultiScale(gray, 1.1, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(im, (x, y), (x + w, y + h),
                      COLOR, THICKNESS)


def face_recognition(im, face_detector, face_recognizer, names):
    # Convert fram from BGR to grayscale
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    # Create a DS faces- array with 4 elements- x,y coordinates top-left corner), width and height
    faces = face_detector.detectMultiScale(gray, 1.1, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(im, (x, y), (x + w, y + h),
                      COLOR, THICKNESS)

        # face_recognizer.predict() method takes the ROI as input and
        # returns the predicted label (id) and confidence score for the given face region.
        id, confidence = face_recognizer.predict(gray[y:y+h, x:x+w])
        print(f"ID: {id}, Confidence: {confidence}")
        if (confidence <= face_recognizer.getThreshold()):
            # print_result(id, confidence, names)
            cv2.putText(im, print_name(id, names), (x+5, y-5), FONT,
                        HEIGHT, COLOR, THICKNESS)
            cv2.putText(im, str(print_confidence(confidence)), (x+5, y+h-5),
                        FONT, HEIGHT, COLOR, THICKNESS)

        # If confidence is less than 100, it is considered a perfect match
        # if confidence <= 60:
        #     id = NAMES[id]
        #     confidence = f"{100 - confidence:.0f}%"
        # else:
        #     id = "Unknown"
        #     confidence = f"{100 - confidence:.0f}%"

        # shift right and up/outside the bounding box from top
        # namepos = (x+5, y-5)
        # shift right and up/intside the bounding box from bottom
        # confpos = (x+5, y+h-5)
        # Display name and confidence of person who's face is recognized
        # cv2.putText(im, str(id), namepos, FONT, HEIGHT, COLOR, THICKNESS)
        # cv2.putText(im, str(confidence), confpos,
        #             FONT, HEIGHT, COLOR, THICKNESS)


def print_confidence(confidence):
    # if 0 <= id < len(names):
    #     return str(f"{100 - confidence:.0f}%")
    # else:
    #     return str('0%')
    return str(f"{100 - confidence:.0f}%")


def print_name(id, names):
    if 0 <= id < len(names):
        return names[id]
    else:
        return str('unknown')


def print_result(id, confidence, names):
    print(
        f"Result ID: {id}, Confidence: {confidence}, Person: {names[id] if id > 0 and id < len(names) else 'unknown'}")
