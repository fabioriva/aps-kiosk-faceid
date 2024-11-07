import cv2

COLOR = (255, 0, 0)  # blue
YELLOW = (0, 255, 255)  # yellow
FONT = cv2.FONT_HERSHEY_COMPLEX
HEIGHT = 1
THICKNESS = 2

COUNT_LIMIT = 30
NAMES = ['None', 'Raffaele Valli', 'Fabio Riva']


def face_capture(im, face_detector, count):
    grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    # Create a DS faces- array with 4 elements- x,y coordinates top-left corner), width and height
    faces = face_detector.detectMultiScale(grey, 1.1, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(im, (x, y), (x + w, y + h),
                      COLOR, THICKNESS)
        if (count[0] < COUNT_LIMIT):
            cv2.putText(im, 'Count: ' + str(int(count[0])), (x+5, y-5),
                        FONT, HEIGHT, COLOR, THICKNESS)
            count[0] += 1  # increment count
        else:
            cv2.putText(im, 'Done: ' + str(int(count[0])), (x+5, y-5),
                        FONT, HEIGHT, COLOR, THICKNESS)


def face_detection(im, face_detector):
    # Convert fram from BGR to grayscale
    grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    # Create a DS faces- array with 4 elements- x,y coordinates top-left corner), width and height
    faces = face_detector.detectMultiScale(grey, 1.1, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(im, (x, y), (x + w, y + h),
                      COLOR, THICKNESS)


def face_recognition(im, face_detector, face_recognizer):
    # Convert fram from BGR to grayscale
    grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    # Create a DS faces- array with 4 elements- x,y coordinates top-left corner), width and height
    faces = face_detector.detectMultiScale(grey, 1.1, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(im, (x, y), (x + w, y + h),
                      COLOR, THICKNESS)

        # face_recognizer.predict() method takes the ROI as input and
        # returns the predicted label (id) and confidence score for the given face region.
        id, confidence = face_recognizer.predict(grey[y:y+h, x:x+w])
        # If confidence is less than 100, it is considered a perfect match
        if confidence <= 60:
            id = NAMES[id]
            confidence = f"{100 - confidence:.0f}%"
        else:
            id = "Unknown"
            confidence = f"{100 - confidence:.0f}%"

        # shift right and up/outside the bounding box from top
        namepos = (x+5, y-5)
        # shift right and up/intside the bounding box from bottom
        confpos = (x+5, y+h-5)
        # Display name and confidence of person who's face is recognized
        cv2.putText(im, str(id), namepos, FONT, HEIGHT, COLOR, THICKNESS)
        cv2.putText(im, str(confidence), confpos,
                    FONT, HEIGHT, COLOR, THICKNESS)
