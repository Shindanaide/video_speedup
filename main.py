import sys
from moviepy import *
from moviepy.editor import *
from moviepy.editor import VideoFileClip, vfx

print("Name of the script", sys.argv[0])

def speedup_process():
	filename = sys.argv[1]
	destination_filename = sys.argv[2]
	multiplier = int(sys.argv[3])
	
	source_video  = VideoFileClip(filename)
	newclip = source_video.speedx(factor=multiplier)
	newclip.write_videofile(destination_filename)
	return newclip

if len(sys.argv) == 1:
	print("INPUT file name missing")
elif len(sys.argv) == 2:
	print("OUTPUT file name missing")
elif len(sys.argv) == 3:
	print("Speed multiplier missing")
elif len(sys.argv) == 4:
	print("In progress...")
	newclip = speedup_process()
	newclip.write_videofile(sys.argv[2])
else:
	print("Too many arguments")