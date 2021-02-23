# configuration file for this app

# timelapse capture
camera_resolution = (2592, 1944)
camera_rotation= 180
datetime_format = "%Y-%m-%d %H_%M_%S"
seconds_to_sleep_until_next_photo = 5
seconds_of_exposure = 2
photo_directory = '/home/pi/Pictures/Timelapse/'
file_extension = '.png'
start_time = 8
end_time = 22
s3_bucket= 'timelapse-dump'
# Video builder

frames_per_second = 5
video_destionation = '/home/pi/Videos/Timelapse/'
video_source_directory = '/home/pi/Pictures/Timelapse/'
video_file_extension = '.avi'