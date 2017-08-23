#!/bin/bash

cd /home/pi/dropbox/bin

echo "Current Activity"

ps -ef | grep main.py
tail ./log/images.log
ls -lrt ./images | tail -5



