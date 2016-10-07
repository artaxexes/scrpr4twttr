#!/usr/bin/python

import twitter
import pymongo



# mongodb connection
mongo_conf = {
	'host' : 'localhost',
	'port' : 27017
} 
mongo = pymongo.MongoClient(mongo_conf['host'], mongo_conf['port'])
mongo_db = mongo.test
mongo_collection = mongo_db.tweets

# twitter connection (https://apps.twitter.com/)
oauth = twitter.OAuth(
	consumer_key = '',	# consumer key (api key) goes here
	consumer_secret = '',	# consumer secret (api secret) goes here
	token = '',		# access token goes here
	token_secret = ''	# access token secret goes here
)
tt = twitter.Twitter(auth = oauth)
tt_query = '#rio2016'
tt_type = 'mixed'
tt_qnt = 100

# search
print 'Searching...',
tts = tt.search.tweets(q = tt_query, result_type = tt_type, count = tt_qnt)

# storage
mongo_collection.insert_many(tts['statuses'])

# log
print '[done]'
print 'Search of %d "%s" %s tweets completed in %.3f seconds' % (tt_qnt, tt_query, tt_type, tts['search_metadata']['completed_in'])
