#!/usr/bin/python

import twitter
import pymongo



# mongodb connection
mongo_conf = {
	"host" : "localhost",
	"port" : 27017
} 
mongo = pymongo.MongoClient(mongo_conf["host"], mongo_conf["port"])
mongo_db = mongo.test
mongo_collection = mongo_db.tweets2

# twitter connection
oauth = twitter.OAuth(
	consumer_key = '',
	consumer_secret = '',
	token = '',
	token_secret = ''
)
twttr = twitter.Twitter(auth = oauth)
twttr_type = "mixed"
twttr_qnt = 100

# search
print "Searching..."
twts = twttr.search.tweets(q = "#rio2016", result_type = twttr_type, count = twttr_qnt)

# storage
mongo_collection.insert_many(twts)

# log
print "Search of %d %s tweets completed in %.3f seconds" % (twttr_qnt, twttr_type, tweets["search_metadata"]["completed_in"])
