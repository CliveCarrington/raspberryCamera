#!/bin/bash

cd /home/pi/dropbox/bin

date >> ./log/images.log

echo "Starting Camera Capture"
python main.py >> ./log/images.log&

