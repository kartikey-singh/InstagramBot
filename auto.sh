#!/bin/sh
# 0 */2 * * * /home/ec2-user/Desktop/InstagramBot/auto.sh>> /tmp/listener.log 2>&1
# */30 * * * * /home/ec2-user/Desktop/InstagramBot/follow.sh>> /tmp/listener1.log 2>&1

echo "Running Script ..."
cd /home/ec2-user/Desktop/InstagramBot
echo $PWD
echo "Activating virtual environment"
. venv/bin/activate
python3.6 instagramBot3.py
echo "Finished"
