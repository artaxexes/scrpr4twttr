#!/usr/bin/python

import sys
import twitter
import pymongo



# config mongodb connection: mongodb url, port, database and collection names
mongo_conf = ('localhost', 27017, 'tweets', 'test')
mongo = pymongo.MongoClient(mongo_conf[0], mongo_conf[1])
mongo_db = mongo[mongo_conf[2]]
mongo_collection = mongo_db[mongo_conf[3]]


# config twitter connection: consumer key, consumer secret, access token, access token secret
oauth = twitter.OAuth(
  consumer_key = '',
  consumer_secret = '',
  token = '',
  token_secret = ''
)


# twitter authentication
print 'connecting... ',
try:
  tt = twitter.Twitter(auth = oauth)
  user = tt.account.settings()
  print '\t[done] connected as', user['screen_name']
except:
  print '\t[error]', sys.exc_info()[1]
  raise


# tweets search
print 'searching... ',
tt_args = ('#temer', 'recent', 100, 'pt')
tts = tt.search.tweets(q = tt_args[0], result_type = tt_args[1], count = tt_args[2], lang = tt_args[3])
print '\t[done] search of %d "%s" %s tweets completed in %.3f seconds' % (tt_args[2], tt_args[0], tt_args[1], tts['search_metadata']['completed_in'])


# tweets storage
print 'storing... ',
try:
  mongo_collection.insert_many(tts['statuses'])
  print '\t[done] %d tweets stored in %s' % (mongo_collection.count(), mongo_collection.full_name)
except:
  print '\t[error]', sys.exc_info()[1]
  raise
finally:
  mongo.close()

print 'finished'
