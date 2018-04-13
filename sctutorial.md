## Supreme Court
**Problem:** At the Supreme Court, what cases are related to Maryland?
**Solution:** Search Supreme Court agenda for Maryland.

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
  
#### Version 2 
Print out in console all recent opinions of the Supreme Court as json
* Get Court Listener API key
* Store in scapikey.json file
* Call in authentication information from scapikey.json
* Import requests
* Use requests.get to call URL: https://www.courtlistener.com/api/rest/v3/clusters/
* Headers for authenticating scapikey.json
* Print json as string in console to test