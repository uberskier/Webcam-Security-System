copyfiles: 
	cp $(filepath) .

#make encoding of faces
makeEncoding:
	python3 src/FaceEncoding.py

#runs main program
runSecurityCamera:
	python3 src/FaceRecWebcam.py

list: 
	ls src/*.py

