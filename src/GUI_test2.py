from guizero import App, Combo, Text, PushButton
from FaceRecWebcam import FaceRecWebcam

app = App(title="My second GUI app", width=300, height=200)
face = FaceRecWebcam()
def runFace():
    face.run()

update_text = PushButton(app, command=runFace, text="Run Security Camera")
app.display()