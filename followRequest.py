#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password
from InstagramAPI import InstagramAPI
import random

InstagramAPI = InstagramAPI("meme.bot.69", "Narutogre8!")
InstagramAPI.login()  # login

def followRequester():
	i = random.randint(1000000000,9999999999)
	for pk in range(i,i + 1000):			
		print(pk)
		InstagramAPI.follow(str(pk))
	return None				

followRequester()