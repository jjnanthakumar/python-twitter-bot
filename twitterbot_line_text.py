import tweepy
from time import sleep
from credentials import *
# Assign twitter Oauth variables
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

# Read lines from sample.txt and close file
test_file=open('sample.txt','r')
file_lines=test_file.readlines()
test_file.close()

# Create a for loop to iterate over file_lines
for line in file_lines:
# print new line with try to catch output errors
    try:
        print(line)
        if line != '\n':
            api.update_status(line)
        # Add an else statement with pass to conclude the conditional statement
        else:
            pass
    except tweepy.TweepError as e:
        print(e.reason)
    sleep(10)
