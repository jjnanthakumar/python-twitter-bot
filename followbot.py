import tweepy
import time
import os
from credentials import *
from config import QUERY, FOLLOW, LIKE, SLEEP_TIME, TWEET_NUMBER
# Assign twitter Oauth variables
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

# name for file saving tweet records
FILE_NAME = 'last_seen.txt'
# Read method for reading last_seen.txt file for reading latest tweets
def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

# Write method to write to last_seen.txt file for reading latest tweets
def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return


def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(15 * 60)

for follower in limit_handled(tweepy.Cursor(api.followers).items()):
    if follower.friends_count < 300:
        print(follower.screen_name)
        for follower in tweepy.Cursor(api.followers).items():
            follower.follow()
