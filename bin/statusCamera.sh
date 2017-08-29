#!/bin/bash

cd ~/Code/raspberryCamera/bin

echo "Current Activity"

ps -ef | grep piCamera.py
tail ./log/images.log
ls -lrt ./images | tail -5

### Checking run status
status=`/bin/ps -ef | grep piCamera.py | wc -l`

if [ $status -eq "1" ] 
then
	echo "Need to start"
	./startPiCamera.sh >./log/images.log &
fi



