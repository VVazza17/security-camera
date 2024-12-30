import subprocess
import time
import boto3
from datetime import datetime

def record_video(duration):
	# Current time to create unique filename
	current_time = datetime.now().strftime("%Y%m%d%H%M%S")
	filename = f'/home/wazza/Videos/video_{current_time}.h264'
	filepath = f'/home/pi/Videos/{filename}'
	
	# Start recording using libcamera-vid
	command = [
	'libcamera-vid',
	'-o', filepath, # Output file
	'-t', str(duration * 1000), # Recording time in ms
	'--inline', # Inline headers for h264
	'--codec', 'h264', # Video codec to use 
	'--width', '1920', # Width of video
	'--height', '1080', # Height of video
	]
	
	print("Video recording started...")
	subprocess.Popen(command).wait()
	print("Video recording stopped...")
	
	upload_to_s3(filepath, filename)
	
def upload_to_s3(file_path, file_name):
	# Create an S3 client
	s3 = boto3.client('s3')
	bucket_name = 'wazzacam-bucket'
	
	print('Uploading to S3...')
	
	try:
		s3.upload_file(file_path, bucket_name, file_name)
		print("Upload complete.")
	except Exception as e:
		print(f"Failed to upload to S3: {e}")

if __name__ == "__main__":
	record_video(60)
