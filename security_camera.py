import subprocess
import time

def record_video(duration):
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
