import tweepy
import time

from os import environ

from tweet_generator import get_tweet

# CONSUMER_KEY = environ['CONSUMER_KEY']
# CONSUMER_SECRET = environ['CONSUMER_SECRET']
# ACCESS_KEY = environ['ACCESS_KEY']
# ACCESS_SECRET = environ['ACCESS_SECRET']

INTERVALE = 60 * 60 * 8  # tweet every 8 hours
INTERVALE = 15

# auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
# auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
# api = tweepy.API(auth)

while True:
    tweet = get_tweet()
    print(tweet)
    # api.update_status(tweet)
    time.sleep(INTERVALE)
