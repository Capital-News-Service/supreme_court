import json
import tweepy
import requests
import pandas as pd


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

money = ["Maryland"] 
for y in money:
    moneysearch = courtdf[courtdf['plain_text'].str.contains(y)]
    if (len(moneysearch) > 0):
        irow = moneysearch.iterrows()
        for j in irow:
            print(j[1]['absolute_url'])