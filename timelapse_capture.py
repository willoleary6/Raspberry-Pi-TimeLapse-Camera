from time import sleep
from picamera import PiCamera
import datetime
import config as Config
import S3Handler
from picamera import Color
import threading
# config


camera = PiCamera(resolution=Config.camera_resolution)
camera.annotate_text_size = 50 # (values 6 to 160, default is 32)
# rotate camera orientation by 180 degrees
camera.rotation = Config.camera_rotation

while(True):
    # lets get the datetime format right
    raw_datetime = datetime.datetime.now()
    # dont need to run this all day
    if raw_datetime.hour >= Config.start_time and raw_datetime.hour < Config.end_time:
        formated_datetime = raw_datetime.strftime(Config.datetime_format)
        # Explicitly open a new file
        filename = Config.photo_directory+formated_datetime+Config.file_extension
        my_file = open(filename, 'wb')
        camera.start_preview()
        sleep(Config.seconds_of_exposure)
        camera.annotate_foreground = Color('black')
        camera.annotate_background = Color('white')
        camera.annotate_text = formated_datetime
        camera.capture(my_file)
        # At this point my_file.flush() has been called, but the file has
        # not yet been closed
        my_file.close()
        # upload to S3
        # Create a Thread with a function without any arguments
        th = threading.Thread(target=S3Handler.upload_file, args=(filename,Config.s3_bucket, filename.rsplit('/', 1)[-1]))
        # Start the thread
        th.start()

        sleep(Config.seconds_to_sleep_until_next_photo)