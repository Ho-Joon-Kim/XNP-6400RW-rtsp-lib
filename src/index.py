from datetime import datetime
import shutil
import uuid
import ffmpeg

class xnp_rtsp:
    def __new__(cls):
        if not hasattr(cls,'instance'):
            cls.instance = super(xnp_rtsp, cls).__new__(cls)
        return cls.instance
    
    def init(self, RTSP_URL, fileLocation = ""):
        self.RTSP_URL = RTSP_URL
        self.fileLocation = fileLocation

    def takeImage(self):
        fileName = datetime.now().strftime("%Y%m%d%H%M%S") + "-" + str(uuid.uuid4()) + ".png"
        stream = ffmpeg.input(self.RTSP_URL, ss=0)
        file = stream.output(fileName, vframes=1)
        file.run(capture_stdout=True, capture_stderr=True)

        if self.fileLocation != "":
            shutil.move(fileName, self.fileLocation + "/" + fileName)
        return fileName