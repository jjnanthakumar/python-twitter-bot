import tweepy
import time

# Assign twitter Oauth variables
consumer_key = 'consumer-key'
consumer_secret = 'consumer-secret'
key = 'privateKey'
secret = 'secret-key'
url = 'https://linktr.ee/somediceguys'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)
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
# Create for loop to like array of hashtags
#create for loop to retweet array of hashtags

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

searchbot_ht1
searchbot_ht2
searchbot_ht3
searchbot_ht4
searchbot_ht5
