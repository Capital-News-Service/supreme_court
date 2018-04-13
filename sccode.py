#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 10:56:54 2018

@author: gmkanik
"""

import json
import tweepy

#opens and reads mvkey.json
sckey={}
with open("sckeys/sckey.json") as file:
    sckey = json.loads(file.read())
  
# Consumer keys and access tokens, used for OAuth
consumer_key = sckey["consumer_key"]
consumer_secret = sckey["consumer_secret"]
access_token = sckey["access_token"]
access_token_secret = sckey["access_token_secret"]

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
# Store access keys in a way to send to Twitter
api = tweepy.API(auth)
tweet = "supreme court"
buildTweet(tweet)

def buildTweet(argument1):
    tweet = "supreme court"
    sendTweet(tweet)

def sendTweet(content):
    try:
        api.update_status(content)
    except tweepy.error.TweepError:
        pass