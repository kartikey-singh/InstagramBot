#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password
from InstagramAPI import InstagramAPI
import random

InstagramAPI = InstagramAPI("meme.bot.69", "Narutogre8!")
InstagramAPI.login()  # login

def followTheFollowers():
	followers = list(InstagramAPI.getTotalSelfFollowers())
	for follower in followers:
		InstagramAPI.follow(follower['pk'])
	return None
followTheFollowers()