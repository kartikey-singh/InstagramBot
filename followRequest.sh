#!/bin/sh
# 0 */2 * * * /home/ec2-user/Desktop/InstagramBot/auto.sh>> /tmp/listener.log 2>&1
# */20 * * * * /home/ec2-user/Desktop/InstagramBot/followRequest.sh>> /tmp/listener1.log 2>&1
# * */2 * * * /home/ec2-user/Desktop/InstagramBot/followTheFollowers.sh>> /tmp/listener2.log 2>&1

echo "Running Script ..."
cd /home/ec2-user/Desktop/InstagramBot
echo $PWD
echo "Activating virtual environment"
. venv/bin/activate
python3.6 followRequest.py
echo "Finished"
