import praw
import urllib.request
import time
import pyautogui
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys

reddit = praw.Reddit(client_id='ylD5CIG9XDPtJA',
					 client_secret='IRZ4big6rczalpMLdKq3t-1FLho',
					 user_agent='my user agent')


file = open("url.txt", "r")
i = 0
data = []
for line in file:
	line = line.strip()
	data.append(line)

# data = i -1
# data = str(data)
# file = open("iteration.txt", "w")
# file.write(data)
# file.close()
 
subreddits = ['PewdiepieSubmissions','memes','dankmemes','pics']

def isposted(url):
	for t in data:
		if t == url:
			return True
	return False

url = []
for submission in reddit.subreddit('PewdiepieSubmissions').new(limit=10):
	print(submission.url[-3:])
	if submission.url[-3:] == 'jpg' or submission.url[-3:] == 'png':
		if isposted(submission.url) == False:
			url.append(submission.url)
		else:
			print('posted')	
		# title(submission.title)
		# urllib.request.urlretrieve(submission.url, str(i) + '.jpg')
	i=i+1

# import sys
# x = 'Modern problems 😥'
# print(x)
# non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
# print(x.translate(non_bmp_map))

# for i in url:
file = open("url.txt", "a")
for i in url:
	file.write(i+'\n')
file.close()

# import os
# os.remove('-99999.jpg')