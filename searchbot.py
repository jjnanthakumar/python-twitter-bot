import tweepy
import time
import os
from credentials import *
from config import QUERY, FOLLOW, LIKE, SLEEP_TIME, TWEET_NUMBER
# Assign twitter Oauth variables
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

# set authentication keys
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(api_key, api_secret)
api = tweepy.API(auth)
twittername ='@somediceguys'
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

# Twitter search strings variables for liking and retweeting trending hashtags
tweetNumber = 20
hashtag1 = '#actualplay'
hashtag1tweets = tweepy.Cursor(api.search, hashtag1).items(tweetNumber)
hashtag2 = '#ttrpg'
hashtag2tweets = tweepy.Cursor(api.search, hashtag2).items(tweetNumber)
hashtag3 = '#pathfinder'
hashtag3tweets = tweepy.Cursor(api.search, hashtag3).items(tweetNumber)
hashtag4 = '#dndstream'
hashtag4tweets = tweepy.Cursor(api.search, hashtag4).items(tweetNumber)
hashtag5 = '#dungeonsandragons'
hashtag5tweets = tweepy.Cursor(api.search, hashtag5).items(tweetNumber)
# Array for hashtags
hashtagArray = ["#dnd", "#actualplay", "#ttrpg", "#dndstream", "#dungeonsandragons", "#pathfinder"]
hashArraytweet = tweepy.Cursor(api.search, hashtagArray).items(tweetNumber)

# Create for loop to like array of hashtags
def likeloop():
    for i in hashArraytweet:
       api.create_favorite(tweet.id)
       print( i + " tweet was liked")

# Create for loop to retweet array of hashtags
def retweetloop():
    for i in hashtagArray:
        tweet.retweet()
        print( i + " tweet was retweeted")


# Search for hashtag variables, like, and retweet
def searchbot_ht1():
    for tweet in hashtag1tweets:
        try:
            tweet.retweet()
            api.create_favorite(tweet.id)
            print( hashtag1 + " found, liked and retweeted")
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(3)


def searchbot_ht2():
    for tweet in hashtag2tweets:
        try:
            tweet.retweet()
            api.create_favorite(tweet.id)
            print( hashtag2 + " found, liked and retweeted")
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(3)


def searchbot_ht3():
    for tweet in hashtag3tweets:
        try:
            api.create_favorite(tweet.id)
            print( hashtag3 + " found, adding to favorites")
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(3)


def searchbot_ht4():
    for tweet in hashtag4tweets:
        try:
            api.create_favorite(tweet.id)
            print( hashtag4 + " found, adding to favorites")
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(3)


def searchbot_ht5():
    for tweet in hashtag5tweets:
        try:
            api.create_favorite(tweet.id)
            print( hashtag5 + " found, adding to favorites")
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(3)

# hashtag1 = '#actualplay'
# hashtag1tweets = tweepy.Cursor(api.search, hashtag1).items(tweetNumber)

for tweet in hashArraytweet:
    api.create_favorite(tweet.id)
    print( tweet + " tweet was liked")

for tweet in hashArraytweet:
    tweet.retweet()
    print( i + " tweet was retweeted")


likeloop()
retweetloop()
