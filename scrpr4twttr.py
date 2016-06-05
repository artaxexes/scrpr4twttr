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
