# import cv2
import numpy as np
from datetime import datetime
# from collections import deque
import upload #upload.py is our dropbox module

upload.auth_dropbox() #authorise this computer to use the dropbox app


# MAIN PROGRAM	



#file_name="test.txt"
file_name = raw_input("What file to upload?   ")

upload.save_to_dropbox(file_name)
	








