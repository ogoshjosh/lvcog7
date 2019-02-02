#!/usr/bin/env python

import os
import glob
from pydub import AudioSegment

video_dir = r'/Users/joshua/Desktop/Audio Files'  # Path where the videos are located
extension_list = ('*.mp4', '*.flv', '*.m4a')

os.chdir(video_dir)
for extension in extension_list:
    for audio in glob.glob(extension):
        mp3_filename = os.path.splitext(os.path.basename(audio))[0] + '.mp3'
        AudioSegment.from_file(audio).export(mp3_filename, format='mp3')
