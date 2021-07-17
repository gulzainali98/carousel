from pytube import YouTube
# misc
import os
import shutil
import math
import datetime
# plots
import matplotlib.pyplot as plt
from frame_extractor import FrameExtractor
# image operation
import cv2
YouTube('https://youtu.be/9bZkp7q19f0').streams.get_highest_resolution().download("static/videos/")
yt = YouTube('http://youtube.com/watch?v=9bZkp7q19f0')
print(yt.title)
print(yt.streams.filter(progressive=True).order_by('resolution')[-1].mime_type.split("/"))
print(yt.title+"."+yt.streams.filter(progressive=True).order_by('resolution')[-1].mime_type.split("/")[-1])
print(yt.streams.all())
# yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download()
