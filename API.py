#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password
import praw
import urllib.request
import sys
import os

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
# Automate Script Calling
from InstagramAPI import InstagramAPI

InstagramAPI = InstagramAPI("meme.bot.69", "Narutogre8!")
InstagramAPI.login()  # login

reddit = praw.Reddit(client_id='ylD5CIG9XDPtJA',
					 client_secret='IRZ4big6rczalpMLdKq3t-1FLho',
					 user_agent='my user agent')

file = open("post.txt", "r")
post_data = []

for line in file:
	line = line.strip()
	post_data.append(line)

def isPost(url):
	for t in post_data:
		if t == url:
			return True
	return False

i = 0 
subreddits = ['woooosh','hmmm','memes','dankmemes','pics',
			'PewdiepieSubmissions','ExpectationVsReality','BeAmazed','Memes_Of_The_Dank',
			'madlads','lostredditors','PornhubComments']

print('POSTS')
file = open("post.txt", "a")
access = True
for sub in subreddits:
	for submission in reddit.subreddit(sub).rising(limit=3):
		if submission.url[-3:] == 'jpg' or submission.url[-3:] == 'png':
			if isPost(submission.url) == False:
				caption = "Posted on r/" + sub + " by u/" + str(submission.author) + " : " +  submission.title + " #memeboi #dank #bot"
				urllib.request.urlretrieve(submission.url, str(i) + '.jpg')
				print(str(submission.author))
				print('Download finished ...')
				print('Uploading ...')
				try :				
					photo_path = '/home/ec2-user/Desktop/InstagramBot/0.jpg'
					InstagramAPI.uploadPhoto(photo_path, caption=caption)
					file.write(str(submission.url)+'\n')
					print('Posted ...')
				except: 			
					print("Couldn't Post")	
				try : 
					os.remove('0.jpg')
				except:
					print("File Not Found")						
			else:
				print('Already posted')
file.close()				

print('Finished :)')



