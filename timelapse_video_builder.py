import cv2
import numpy as np
import glob
import os
import datetime
import config as Config

raw_datetime = datetime.datetime.now()
formated_datetime = raw_datetime.strftime(Config.datetime_format)
img_array = []


for filename in sorted(glob.glob(Config.video_source_directory+'*'+Config.file_extension), key=os.path.getmtime):
    img = cv2.imread(filename)
    if img is not None:
        height, width, layers = img.shape
        size = (width,height)
        img_array.append(img)


out = cv2.VideoWriter(
    Config.video_destionation+formated_datetime+Config.video_file_extension,
    cv2.VideoWriter_fourcc(*'DIVX'),
    Config.frames_per_second,
    size
    )

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()