# Twitter bot to read, reply, and retweet
# from interaction
# tutorial link https://www.youtube.com/watch?v=ewq-91-e2fw&list=WL&index=2&t=112s
# stopped at 13:40
import tweepy
import time
import os
# Assign twitter Oauth variables

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
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

# For loop to search and like hashtag list
def search_and_like():
    for tweet in hashtaglist:
        api.create_favorite(tweet.id)
        print( tweet + " found, adding to favorites")

search_and_like
