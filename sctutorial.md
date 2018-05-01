## Supreme Court
**Problem:** At the Supreme Court, what cases are related to Maryland?
**Solution:** Search Supreme Court opinions for Maryland.

#### Version 1
Sends out a tweet when the program runs to a Twitter account.
* Create a gmail account for bot
  - supremecourtmdcns@gmail.com
* Create a Twitter account using gmail account
  - @supreme_c_md
* Get keys for Twitter account at apps.twitter.com
* Create GitHub repo with 4 files: sctutorial.md, sckey.json, readme.md, GitIgnore, & sccode.py
* Write the following code in pskey.json:
  - consumer key, consumer key secret, access token, & access token secret
* Write the following code in pscode.py:
  - Import Json & Tweepy
  - Call in authentication information from pskey.json
  - Store them so they can be passed into Twitter
  - Create keyword to tweet out
  - Tweet out keyword with authentication to test
```
import json
import tweepy

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

tweet = "supreme court"
buildTweet(tweet)
```
  
#### Version 2 
Put all recent opinions of the Supreme Court in a dataframe
* Get Court Listener API key
* Store in scapikey.json file
* Call in authentication information from scapikey.json
* Import requests
* Use requests.get to call URL: https://www.courtlistener.com/api/rest/v3/clusters/?court_id=scotus 
* Headers for authenticating scapikey.json
* Put results of json into dataframe
```
import requests
import pandas as pd

#opens and reads scapikey.json
scapikey={}
with open("sckeys/scapikey.json") as file:
    scapikey = json.loads(file.read())
#authenticate and calls api to print text
sc_api_key = scapikey["sc_api_key"]

#calls court listener api and puts results into json and dataframe
urlcourt = 'https://www.courtlistener.com/api/rest/v3/clusters/?court_id=scotus'
headers = {'SC-API-KEY': sc_api_key}
responsecourt = requests.get(urlcourt, headers=headers)
jsoncourt = responsecourt.json()
datacourt = jsoncourt.get('results')
courtdf = pd.DataFrame(datacourt)
```

#### Version 3
* Iterate over column plain_text to find text file of list of words
* If found, print out event in console
```
#import list of Maryland terms
scterms = []
with open('scterms.txt', 'r') as s:
    scterms = s.read().splitlines()

for t in scterms:
    search = courtdf[courtdf['plain_text'].str.contains(t)]
    print(t)
    if (len(search) > 0):
        irow = search.iterrows()
        for r in irow:
            print(r[1]['absolute_url'])
```
#### Version 4
* Get yesterday's date
* Search for date in data frame under date_created by iterating over rows
* If found, print out event in console
```
def getDate():
    yesterday = datetime.now() - timedelta(days=1)
    date = yesterday.strftime('%Y-%m-%d')
    print(date)
    return date

#search for md locations only for today
date = getDate()
courtdf = courtdf.replace(np.nan, '', regex=True)
scdate = courtdf[courtdf['date_created'].str.contains(date)]
if (len(scdate) > 0):
    irow = scdate.iterrows()
    for i in irow:
        print(i[1]['date_created'])
```            
#### Version 5
* Create text file of list of terms related to Maryland
* Search for list of terms in recent opinions in plain_text by iterating over rows
* If found, tweet out date
```
#import list of Maryland terms
scterms = []
with open('scterms.txt', 'r') as s:
    scterms = s.read().splitlines()
    
for t in scterms:
    search = scdate[scdate['plain_text'].str.contains(t)]
    if (len(search) > 0):
        irow = search.iterrows()
        for r in irow:
            print(r[1]['absolute_url'])
            buildTweet(date, r[1]['download_url'])
```