import face_recognition
import imutils
import pickle
import time
import cv2
import os

cfp = os.path.dirname(cv2.__file__) + "/data/haarcascade_frontalface_alt2.xml"

fc = cv2.CascadeClassifier(cfp)

data = pickle.loads(open('face_enc', "rb").read())

image = cv2.imread('../Camera-Pictures/BandO.jpg')
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = fc.detectMultiScale(gray,
scaleFactor=1.1,
minNeighbors=6,
minSize=(60, 60),
flags=cv2.CASCADE_SCALE_IMAGE)

encodings = face_recognition.face_encodings(rgb)
names = []
for encoding in encodings:
    matches = face_recognition.compare_faces(data["encodings"], encoding)
    name = "Unknown"
    if True in matches:
        matchedIdxs = [i for (i, b) in enumerate(matches) if b]
        count = {}
        for i in matchedIdxs:
            name = data["names"][i]
            count[name] = count.get(name, 0) + 1
            name = max(count, key=count.get)
            names.append(name)

for ((x, y, w, h), name) in zip(faces, names):
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.putText(image, name, (x,y), cv2.FONT_HERSHEY_SIMPLEX,
    0.75, (0,255,0), 2)
    resize = cv2.resize(image, (960, 960))
    cv2.imshow("Frame", resize)
    cv2.waitKey(0)