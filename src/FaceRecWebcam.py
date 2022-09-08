import face_recognition
import imutils
import pickle
import time
import cv2

 
print("[INFO] loading encodings...")
data = pickle.loads(open('encoding', "rb").read())
 
print("Streaming started")
video_capture = cv2.VideoCapture(0)
# loop over frames from the video file stream
SavedPeople = {}
timeTimer = time.perf_counter()
timeTimer =- 12
while True:
    # grab the frame from the threaded video stream
    ret, frame = video_capture.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    boxes = face_recognition.face_locations(rgb, model="hog")
    encodings = face_recognition.face_encodings(rgb, boxes)
    names = []
    
    timeTemp = time.perf_counter()
    if (timeTemp - timeTimer) > 10 and (timeTemp - timeTimer) < 12: 
        print("sms")
        time.sleep(3)
        SavedPeople.clear()

    # loop over the facial embeddings incase
    for encoding in encodings:
        timeTimer = time.perf_counter()
       #Compare encodings with encodings in data["encodings"]
       #Matches contain array with boolean values and True for the embeddings it matches closely
       #and False for rest
        matches = face_recognition.compare_faces(data["encodings"], encoding)
        name = "Unknown"
        
        if True in matches:
            matchedIdxs = [i for (i, b) in enumerate(matches) if b]
            counts = {}

            for i in matchedIdxs:
                name = data["names"][i]
                counts[name] = counts.get(name, 0) + 1
            
            name = max(counts, key=counts.get)
 
        names.append(name)
        
        # loop over the recognized faces
    for ((top, right, bottom, left), name) in zip(boxes, names):
        # rescale the face coordinates
        # draw the predicted face name on the image
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        y = top - 15 if top - 15 > 15 else top + 15
        cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
            0.75, (0, 255, 0), 2)
        if len(SavedPeople) == 0:
            SavedPeople[name] = frame
        elif name in SavedPeople == False:
            SavedPeople[name] = frame

    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()