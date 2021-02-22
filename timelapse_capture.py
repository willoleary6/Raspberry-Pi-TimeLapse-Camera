from time import sleep
from picamera import PiCamera
import datetime
# config
camera_resolution = (2592, 1944)
camera_rotation= 180
datetime_format = "%Y_%m_%d_%H_%M_%S"
seconds_to_sleep_until_next_photo = 10
seconds_of_exposure = 2
photo_directory = '/home/pi/Pictures/Timelapse/'
file_extension = '.png'


camera = PiCamera(resolution=camera_resolution)

# rotate camera orientation by 180 degrees
camera.rotation = camera_rotation
while(True):
    # lets get the datetime format right
    raw_datetime = datetime.datetime.now()
    formated_datetime = raw_datetime.strftime(datetime_format)
    # Explicitly open a new file called my_image.jpg
    my_file = open(photo_directory+formated_datetime+file_extension, 'wb')
    camera.start_preview()
    sleep(seconds_of_exposure)

    camera.capture(my_file)
    # At this point my_file.flush() has been called, but the file has
    # not yet been closed
    my_file.close()
    sleep(seconds_to_sleep_until_next_photo)