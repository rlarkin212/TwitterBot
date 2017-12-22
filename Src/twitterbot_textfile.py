# Import our Twitter credentials from credentials.py
from Credentials import *
import tweepy
from time import sleep

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

myfile = open('lilpump.txt','r')
fileLines = myfile.readlines()
myfile.close()

#loop to go over lines
for line in fileLines:

    try:
        print(line)
        if line != '\n':
            api.update_status(line)
        else:
            pass
    except tweepy.TweepError as e:
        print(e.reason)
    
    sleep(5)