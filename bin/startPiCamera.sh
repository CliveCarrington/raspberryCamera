#!/bin/bash

cd /home/pi/Code/raspberryCamera/bin

sleep 4s
sudo modprobe bcm2835-v4l2

sleep 4s


date >> ./log/images.log

echo "Starting Camera Capture"
python piCamera.py >> ./log/images.log&

