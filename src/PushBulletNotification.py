import os
from pushbullet import PushBullet

class pushBullet():
    def __init__(self, access_token):
        self.pb = PushBullet(access_token)
        self.data = "Security Camera Spotted Someone"
        pass

    def text(self, dict):
        text = ""
        for key in dict:
            for keys in dict[key]:
                if keys == "date":
                    time = dict[key][keys].strftime("%m-%d-%y %I:%M:%S%p")
                    text = (text + time)
                elif keys != "newPerson":
                    text = (keys + " seen at ")
                    self.frame = dict[key][keys]
                    self.name = keys
            self.pb.push_note(self.data, text)
            self.image()
        pass

    def image(self):
        with open(self.frame, "rb") as pic:
            imgName = self.name + ".jpg"
            file_data = self.pb.upload_file(pic, imgName)
        self.pb.push_file(**file_data)
        if os.path.exists(self.frame):
            os.remove(self.frame)
        pass