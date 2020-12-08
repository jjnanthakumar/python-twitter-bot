# Twitter bot to read, reply, and retweet
# from interaction
# tutorial link https://www.youtube.com/watch?v=ewq-91-e2fw&list=WL&index=2&t=112s
# stopped at 13:40
import tweepy
import time
import os


# Assign twitter Oauth variables via global system vars
consumer_key = os.environ.get('BOT_CON_KEY')
consumer_secret = os.environ.get('BOT_CON_SECRET')
apikey = os.environ.get('BOT_API_KEY')
apisecret = os.environ.get('BOT_API_SECRET')
url = os.environ.get('BOT_SHARE_URL')
auth = tweepy.OAuthHandler(os.environ.get('BOT_CON_KEY'), os.environ.get('BOT_CON_SECRET'))
#auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(os.environ.get('BOT_CON_KEY'), os.environ.get('BOT_CON_SECRET'))
api = tweepy.API(auth)
# Twitter search strings variables for liking and retweeting trending hashtags
tweetNumber = 10
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

hashtaglist = ['#actualplay', '#ttrpg', '#PathFinder', '#dndstream', '#dungeonsanddragons', '#DnD', '#dnd' ]

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

# For loop to search and like hashtag list
def search_and_like():
    for tweet in hashtaglist:
        api.create_favorite(tweet.id)
        print( tweet + " found, adding to favorites")

def searchbot_ht1():
    for tweet in hashtag1tweets:
        try:
            api.create_favorite(tweet.id)
            print( hashtag1 + " found, adding to favorites")
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(3)

searchbot_ht1

#while True:
#    search_and_like
