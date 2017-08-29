#!/bin/bash

cd ~/Code/raspberryCamera/bin

echo "Checking Current Camera Heath" > ./log/cameraHealth.log

echo " " >> ./log/cameraHealth.log
echo "Processes Running" >> ./log/cameraHealth.log
ps -ef | grep piCamera.py >> ./log/cameraHealth.log

echo " " >> ./log/cameraHealth.log
echo " " >> ./log/cameraHealth.log
echo "Tail of the images log file" >> ./log/cameraHealth.log
tail -100  ./log/images.log >> ./log/cameraHealth.log

echo " " >> ./log/cameraHealth.log
echo " " >> ./log/cameraHealth.log
echo "Listing of the images directory" >> ./log/cameraHealth.log
ls -lrt ./images/* | tail -25 >> ./log/cameraHealth.log

cd log

s3cmd put cameraHealth.log s3://len.carrington.picam2/images/cameraHealth.log

