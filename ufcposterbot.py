# ufcposterbot

import tweepy as tp
import config
import time
import os

# log in to twitter account api
auth = tp.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_secret)
api = tp.API(auth)

# iterates through images in the poster folder and tweets one every 24 hours
os.chdir('ufcposters')
for poster_image in os.listdir('.'):
    api.update_with_media(poster_image)
    time.sleep(86400)
