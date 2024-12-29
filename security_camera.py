import subprocess
import time
from datetime import datetime

def record_video(duration):
	# Current time to create unique filename
	current_time = datetime.now().strftime("%Y%m%d%H%M%S")
	filename = f'/home/wazza/Videos/video_{current_time}.h264'
	
	# Start recording using libcamera-vid
	command = [
	'libcamera-vid',
	'-o', '/home/wazza/Videos/video.h264', # Output file
	'-t', str(duration * 1000), # Recording time in ms
	'--inline', # Inline headers for h264
	'--codec', 'h264', # Video codec to use 
	'--width', '1920', # Width of video
	'--height', '1080', # Height of video
	]
	
	print("Video recording started...")
	process = subprocess.Popen(command) # Starts recording
	time.sleep(duration) # Waits for duration to pass
	process.terminate() # Stops recording
	print("Video recording stopped...")
	
if __name__ == "__main__":
	record_video(60)
