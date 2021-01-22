# Python-Twitter-Bot
Python Twitter Bot

### Requirements
To use this twitter bot you'll need Python 3, a Twitter account, twitter application variables, and the python [tweepy module](https://docs.tweepy.org/en/latest/).

$ pip install tweepy
 or
$ pip install -r Requirements.txt

### Variables
To use this bot, you will need to add the twitter application keys and add them to the credentials.py.

* consumer_key = 'your_consumer_key'
* consumer_secret = 'your_consumer_secret'
* access_token = 'your_access_token'
* access_token_secret = 'your_access_token_secret'
* twittername ='@somediceguys' (for direct message bot)

Note: Its important to that you secure the credentials.py file and not share it publicly with your twitter keys on github.

### Twitter Developer setup
You need to create a new application on Twitter. Either you can use your current account or you can create a new one. I personally would create a new account for your bot so that your main Twitter account doesn't get banned.
To create a new application on Twitter, go to https://apps.twitter.com/

Fill all details required to create the new app. After that  you can click on the "Key and Access Token" tab in app settings. You will also get the apps consumer key, api key, access token, and access token secret keys to add to your credentials.py

## Test the Bot
Once you have the credentials setup you can run the bot_test.py to run and tweet lines from the sample.txt file.

$ python twitter_line_text.py

You can change the sample text file to whatever you want. To do som change the line in the twitterbot_line_text.py that says my_file=open('sample.txt','r') and change it the the filename of your choice instead of 'sample.txt'.

# Twitter bots for each occasion: Tweet, Retweet, Like, and Follow

* followbot.py - follows new followers of specified twitter account.
* replybot - reply to mentions of you with specific matched words.
* searchbot - search's through an array of hastags listed and retweets anything that matches it.
* directbot - Sends a direct message to any new followers that follow you
* likebot - likes tweets if LIKES = True in config.py 

You can change the parameters of the QUERY in config.py to change the hashtags you want to retweet or follow. You can also modify the code to tweet specific things, or follow specific people or trends.

### Deployment tips
You can deploy this twitterbot using Jenkins or some other online hosting platform. Changes to the sleep time on the bot should be adjusted if you plan on running the bot all day.
