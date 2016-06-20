#!/usr/bin/python

import csv
from twitter import *

token = raw_input("Twitter token: ")
token_secret = raw_input("Twitter token secret: ")
consumer_secret = raw_input("Twitter consumer secret: ")
consumer_key = raw_input("Twitter consumer key: ")

config = {
	"token" : token,
	"token_secret" : token_secret,
	"consumer_secret" : consumer_secret,
	"consumer_key" : consumer_key,
}

twitter = Twitter(auth = OAuth(config["token"], config["token_secret"], config["consumer_key"], config["consumer_secret"]))

query = raw_input("See what's happening right now: ")
tweets = twitter.search.tweets(q = query, result_type = "recent", count = 50)
print "\nSearch completed in %.3f seconds" % (tweets["search_metadata"]["completed_in"])
print "\n50 more recent results:\n"
for tweet in tweets["statuses"]:
	print "@%s tweeted: %s" % (tweet["user"]["screen_name"], tweet["text"])
../scrpr.py


'''

#!/usr/bin/python
# http://github.com/ideoforms/python-twitter-examples
# based on tweepy
import tweepy
auth = tweepy.OAuthHandler('hmryIyCil5XRS1gOC62h3A6uo', 'KJB3dgIoMiZIcMjy1ZjSYXg4BtPmGcopKQgRqrrf4MiJs47VcJ')
auth.set_access_token('3350825781-VKx3pi042mRvvGuMzfPVNaJUgSBX22XOHnxhD7T', 'z870lC17BLNyTuLxywG0F93kDkNAI6SCNfOINiueGQzSd')
api = tweepy.API(auth)
public_tweets = api.home_timeline()
for tweet in public_tweets:
	print '* ' + tweet.text
# based on https://pypi.python.org/pypi/twitter from twitter
config = {
	"token" : "3350825781-VKx3pi042mRvvGuMzfPVNaJUgSBX22XOHnxhD7T",
	"token_secret" : "z870lC17BLNyTuLxywG0F93kDkNAI6SCNfOINiueGQzSd",
	"consumer_secret" : "KJB3dgIoMiZIcMjy1ZjSYXg4BtPmGcopKQgRqrrf4MiJs47VcJ",
	"consumer_key" : "hmryIyCil5XRS1gOC62h3A6uo",
}
twttr = Twitter(auth=OAuth(config["token], config["token_secret"], config["consumer_secret"], config["consumer_key"]))
trends = api.trends_place()
for trend in trends:
	print trend
query = raw_input("Veja o que esta acontecendo agora: #")
print config['consumer_key'] twttr.search.tweets(q="#MinhaCasaMinhaVida")

'''
