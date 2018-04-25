import json
import tweepy
import requests
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

#opens and reads sckey.json
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

def buildTweet(argument1):
    tweet = "supreme court"      
    sendTweet(tweet)

def sendTweet(content):
    try:
        api.update_status(content)
    except tweepy.error.TweepError:
        pass
    
#opens and reads scapikey.json
scapikey={}
with open("sckeys/scapikey.json") as file:
    scapikey = json.loads(file.read())
#authenticate and calls api to print text
sc_api_key = scapikey["sc_api_key"]

#calls court listener api and puts results into json and dataframe
urlcourt = 'https://www.courtlistener.com/api/rest/v3/opinions/?cluster__docket__court__id=scotus'
headers = {'SC-API-KEY': sc_api_key}
responsecourt = requests.get(urlcourt, headers=headers)
jsoncourt = responsecourt.json()
datacourt = jsoncourt.get('results')
courtdf = pd.DataFrame(datacourt)

#import yesterday's date
def getDate():
    yesterday = datetime.now() - timedelta(days=1)
    date = yesterday.strftime('%Y-%m-%d')
    print(date)
    return date

#search for md locations only for today
#date = getDate()
#courtdf = courtdf.replace(np.nan, '', regex=True)
#scdate = courtdf[courtdf['date_created'].str.contains(date)]
#if (len(scdate) > 0):
#    irow = scdate.iterrows()
#    for i in irow:
#        print(i[1]['date_created'])

#import list of Maryland terms
scterms = []
with open('scterms.txt', 'r') as s:
    scterms = s.readlines()

for t in scterms:
    search = courtdf[courtdf['plain_text'].str.contains(t)]
    print(t)
    if (len(search) > 0):
        irow = search.iterrows()
        for r in irow:
            print(r[1]['absolute_url'])