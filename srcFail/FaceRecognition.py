import face_recognition
import argparse
import pickle
import cv2


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="input image path")
args=vars(ap.parse_args())

print("[INFO] loading encodings...")
data = pickle.loads(open('encoding', "rb").read())

image=cv2.imread(args["image"])

rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

print("[INFO] recognizing faces...")
boxes = face_recognition.face_locations(rgb, model="hog")

encodings = face_recognition.face_encodings(rgb, boxes)

names=[]
# loop over the facial embeddings
for encoding in encodings:
	# attempt to match each face in the input image to our known
	# encodings
	matches = face_recognition.compare_faces(data["encodings"], encoding)
	name = "Unknown"

	if True in matches:

		matchedIdxs = [i for (i, b) in enumerate(matches) if b]
		counts={}

		for i in matchedIdxs:
			name= data["names"][i]
			counts[name]= counts.get(name, 0) + 1


		name = max(counts, key=counts.get)

	names.append(name)



# loop over the recognized faces
for ((top, right, bottom, left), name) in zip(boxes, names):
	# draw the predicted face name on the image
	cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
	y = top - 15 if top - 15 > 15 else top + 15
	cv2.putText(image, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
		0.75, (0, 255, 0), 2)
 
# show the output image
resize = cv2.resize(image, (960, 960))
cv2.imshow("Image", resize)
cv2.waitKey(0)