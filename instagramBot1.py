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
# Upload on server ?? How py auto gui will work and chrome ??ed
# Automate Script Calling

def site_login(title):
	# Opening Instagram in Mobile Version
	mobile_emulation = { "deviceName": "Nexus 5" }
	chrome_options = Options()
	chrome_options.add_argument("--window-size=200,700")
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
	
	try:
		driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button[2]').click()
		time.sleep(3)
	except:
		print("# Add Home Notif")
	# try:
	# driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[3]/button[2]').click()
	# time.sleep(3)
	# except:		
	# print("# Turn Off Notif")
	try:
		driver.find_element_by_xpath('//*[@id="react-root"]/section/nav[2]/div/div/div[2]/div/div/div[3]/span').click()
		time.sleep(3)
	except:
		print("# Post")
	
	# Going to Desktop
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

	try:
		driver.find_element_by_xpath('//*[@id="react-root"]/section/div[2]/div[2]/div/div/div/button[1]/span').click()
		time.sleep(3)
	except:
		print("# Adjusting Image Size")
	try:		
		driver.find_element_by_xpath('//*[@id="react-root"]/section/div[1]/header/div/div[2]/button').click()
		time.sleep(3)
	except:
		print("# Going to Next Page to Post")
	
	try:
		title = title.translate(non_bmp_map)
		driver.find_element_by_xpath('//*[@id="react-root"]/section/div[2]/section[1]/div[1]/textarea').send_keys(title)
		driver.find_element_by_xpath('//*[@id="react-root"]/section/div[1]/header/div/div[2]/button').click()
	# time.sleep(3)
	except:
		print("# Giving Content and Sharing")
	
	# driver.close()		
	return None

reddit = praw.Reddit(client_id='ylD5CIG9XDPtJA',
					 client_secret='IRZ4big6rczalpMLdKq3t-1FLho',
					 user_agent='my user agent')

# file = open("iteration.txt", "r")
# data = file.read()
# i = int(data)
i = 0 
subreddits = ['woooosh','hmmm','memes','dankmemes','pics','PewdiepieSubmissions']

for sub in subreddits:
	for submission in reddit.subreddit(sub).hot(limit=5):
		if submission.url[:9] == 'https://i':
			title = "Posted on r/" + sub + " by u/" + str(submission.author) + " : " +  submission.title + " #memeboi #dank #bot"
			urllib.request.urlretrieve(submission.url, str(i) + '.jpg')
			print(str(submission.author))
			print('Download finished ...')
			print('Uploading ...')
			try :
				site_login(title)
				print('Done ...')
			except: 			
				print("Couldn't Post")	
			try : 
				os.remove('0.jpg')
			except:
				print("File Not Found")	

# data = i+1
# data = str(data)
# file = open("iteration.txt", "w")
# file.write(data)
# file.close()
print('Finished :)')
