
from picamera2 import Picamera2, Preview
from time import sleep
import os

###### CONFIG ######
NON_GUI = False
FILE_PREFIX = '/home/benny/Desktop'
###### END CONFIG ######


def take_picture(filename):
    with Picamera2() as camera:
        camera_config = camera.create_preview_configuration()
        camera.resolution = (1024, 768)
        if NON_GUI:
            camera.start_preview(Preview.DRM)
        else:
            camera.start_preview(Preview.QTGL)
        # Camera warm-up time
        camera.start()
        sleep(2)
        camera.capture_file(filename)

take_picture(FILE_PREFIX + os.sep + 'image.jpg')