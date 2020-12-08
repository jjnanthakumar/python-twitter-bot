# Twitter bot to retweet, follow, and DM people who interact with
# specific user
# from interaction
# tutorial link https://www.youtube.com/watch?v=ewq-91-e2fw&list=WL&index=2&t=112s
# stopped at 13:40
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
twittername ='@somediceguys'
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

# Send reply back to users
def reply():
    # Returns the 20 most recent mentions, including retweets.
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
    # for loop to print tweet id and tweet in order
    # and responds to last seen tweet with a thank you
    for tweet in reversed(tweets):
        if twittername in tweet.full_text.lower():
            print(str(tweet.id) + ' - ' + tweet.full_text)
            api.create_favorite(tweet.id)
            #api.update_status("@" + tweet.user.screen_name + " Thank you!", tweet.id)
            store_last_seen(FILE_NAME, tweet.id)

# Retweet people who mention twittername
def diceguys_mentions():
    # Returns the 20 most recent mentions, including retweets.
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
    # for loop to like and retweet any
    # tweets containing @somediceguys
    for tweet in reversed(tweets):
        if twittername in tweet.full_text.lower():
            print("New twitter interaction")
            tweet.retweet()
            api.create_favorite(tweet.id)

# Send DM to new followers
def direct_message():
    # Returns the 20 most recent mentions, including retweets.
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
    new_followers = API.followers(user)
    # for loop to send direct messages to new followers
    for i in reversed(new_followers):
        if '@somediceguys' in tweet.full_text.lower():
            api.get_direct_message(tweet.id)
            api.send_direct_message(twitter_user, 'Thank you for following us. We are just getting started with our adventure. Feel free to listen to our podcast here https://linktr.ee/somediceguys ')
            print("New twitter follower, DM sent ")

#Follow back users who follow you
