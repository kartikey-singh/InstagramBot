import praw
import urllib.request
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import sys
import os

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
# Automate Script Calling

def login():
	# Opening Instagram in Mobile Version
	mobile_emulation = { "deviceName": "Nexus 5" }
	chrome_options = Options()
	chrome_options.add_argument("--window-size=400,700")
	chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
	driver = webdriver.Chrome(executable_path='//home/kartikey/Desktop/Files/Insta_Bot/chromedriver',chrome_options=chrome_options)
	driver.get ('https://www.instagram.com/accounts/login/')
	time.sleep(3)
	driver.find_element_by_name("username").send_keys('meme.bot.stealer@gmail.com')
	passwordInput = driver.find_element_by_name("password")
	passwordInput.send_keys('*******')
	passwordInput.send_keys(Keys.ENTER)
	time.sleep(3)
	try:
		driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/button').click()
		time.sleep(3)
	except:
		print("# Not Now Login Notif")
	return driver

def fileaccess(access):
	# Going to Desktop
	if access == True:
		pyautogui.press(['down', 'down', 'down','down'])
		pyautogui.press('enter') 
		time.sleep(3)
		# Going to Files
		pyautogui.press(['down', 'down', 'down','down','down'])
		pyautogui.press('enter') 
		time.sleep(3)
		# Going to InstaBot
		pyautogui.press(['down', 'down'])
		# Clicking First Image
		pyautogui.press('enter') 
		time.sleep(3)
		# Opening the image in Insta
		pyautogui.press('enter') 
		time.sleep(3)
	else:	
		pyautogui.press('enter') 
		time.sleep(3)	
	return None

def post(driver,title,access) :
	try:
		driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button[2]').click()
		time.sleep(3)
	except:
		print("# Add Home Notif")
	try:
		driver.find_element_by_xpath('//*[@id="react-root"]/section/nav[2]/div/div/div[2]/div/div/div[3]/span').click()
		time.sleep(3)
	except:
		print("# Post")
	
	fileaccess(access)

	try:
		driver.find_element_by_xpath('//*[@id="react-root"]/section/div[2]/div[2]/div/div/div/button[1]/span').click()
		time.sleep(3)
	except:
		print("# Adjusting Image Size Failed")
	try:		
		driver.find_element_by_xpath('//*[@id="react-root"]/section/div[1]/header/div/div[2]/button').click()
		time.sleep(3)
	except:
		print("# Going to Next Page to Post Failed")
	
	try:
		title = title.translate(non_bmp_map)
		driver.find_element_by_xpath('//*[@id="react-root"]/section/div[2]/section[1]/div[1]/textarea').send_keys(title)
		driver.find_element_by_xpath('//*[@id="react-root"]/section/div[1]/header/div/div[2]/button').click()
		time.sleep(3)
	except:
		print("# Giving Content and Sharing Failed")
	# driver.close()
	return None

# def story(driver,access):
# 	# try:
# 	driver.find_element_by_xpath('//*[@id="react-root"]/section/nav[1]/div/div/header/div/div[1]/button/span').click()
# 	time.sleep(3)
# 	# except:
# 	print("#Opening Story Mode Failed")

# 	fileaccess(access)		
		
# 	# try:
# 	driver.find_element_by_xpath('//*[@id="react-root"]/section/footer/div/button/span').click()
# 	time.sleep(3)
# 	# except:
# 	print("#Add to Your Story Failed")	
# 	return None	

reddit = praw.Reddit(client_id='ylD5CIG9XDPtJA',
					 client_secret='IRZ4big6rczalpMLdKq3t-1FLho',
					 user_agent='my user agent')

file = open("post.txt", "r")
post_data = []
for line in file:
	line = line.strip()
	post_data.append(line)

# file = open("story.txt", "r")
# story_data = []
# for line in file:
# 	line = line.strip()
# 	story_data.append(line)

def isPost(url):
	for t in post_data:
		if t == url:
			return True
	return False

# def isStory(url):
# 	for t in story_data:
# 		if t == url:
# 			return True
# 	return False
i = 0 
subreddits = ['woooosh','hmmm','memes','dankmemes','pics',
			'PewdiepieSubmissions','ExpectationVsReality','BeAmazed','Memes_Of_The_Dank',
			'madlads','lostredditors','PornhubComments']

driver = login()

print('POSTS')
file = open("post.txt", "a")
access = True
for sub in subreddits:
	for submission in reddit.subreddit(sub).rising(limit=3):
		if submission.url[-3:] == 'jpg' or submission.url[-3:] == 'png':
			if isPost(submission.url) == False:
				title = "Posted on r/" + sub + " by u/" + str(submission.author) + " : " +  submission.title + " #memeboi #dank #bot"
				urllib.request.urlretrieve(submission.url, str(i) + '.jpg')
				print(str(submission.author))
				print('Download finished ...')
				print('Uploading ...')
				try :				
					post(driver,title,access)
					access = False
					try:
						driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[3]/button[2]').click()
						time.sleep(3)
					except:		
						print("# Turn Off Notification Not Found")
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

# print('STORIES')
# stories = []
# access = True
# for sub in subreddits:
# 	for submission in reddit.subreddit(sub).rising(limit=2):
# 		if submission.url[-3:] == 'jpg' or submission.url[-3:] == 'png':
# 			if isStory(submission.url) == False:
# 				urllib.request.urlretrieve(submission.url, str(i) + '.jpg')
# 				print(str(submission.author))
# 				print('Download finished ...')
# 				print('Uploading ...')
# 				# try :				
# 				story(driver,access)
# 				access = False
# 					# try:
# 					# 	driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[3]/button[2]').click()
# 					# 	time.sleep(3)
# 					# except:		
# 					# 	print("# Turn Off Notification Not Found")
# 				stories.append(submission.url)	
# 				print('Done ...')
# 				# except: 			
# 				# 	print("Couldn't Post")	
# 				# try : 
# 				os.remove('0.jpg')
# 				# except:
# 				print("File Not Found")	

# 			else:
# 				print('Already a story')		



# file = open("story.txt", "a")
# for i in stories:
# 	file.write(i+'\n')
# file.close()

print('Finished :)')
