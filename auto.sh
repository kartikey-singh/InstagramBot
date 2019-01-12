#!/bin/sh
echo "Running Script ..."
cd /home/ec2-user/Desktop/InstagramBot
echo $PWD
echo "Activating virtual environment"
. venv/bin/activate
python3.6 API.py
echo "Finished"
