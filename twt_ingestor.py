#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import twitter
import pymongo





'''

    twitter

'''

oauth = twitter.OAuth(
  consumer_key = '',
  consumer_secret = '',
  token = '',
  token_secret = ''
)

print 'connecting...'

try:
  tt = twitter.Twitter(auth = oauth)
  user = tt.account.settings()
  print '[done] connected as', user['screen_name']
except:
  print '[error]', sys.exc_info()[1]
  raise

print 'searching...'

# paging timeline twitter (https://dev.twitter.com/rest/public/timelines)
# 1st request
tt_args = ('#PEC241', 'mixed', 500, 'pt')
tts = tt.search.tweets(q = tt_args[0], result_type = tt_args[1], count = 100, lang = tt_args[3])
stts = tts['statuses']
seconds = tts['search_metadata']['completed_in']
# other requests
for i in range((tt_args[2]/100) - 1):
  min_id = reduce(lambda x, y: x if x <= y else y, map(lambda k: k['id'], tts['statuses']))
  since_id = tts['search_metadata']['since_id']
  tts = tt.search.tweets(q = tt_args[0], result_type = tt_args[1], count = 100, lang = tt_args[3], max_id = min_id - 1, since_id = since_id)
  stts += tts['statuses']
  seconds += tts['search_metadata']['completed_in']

print '[done] search of %d "%s" %s tweets completed in %.2f seconds' % (len(stts), tt_args[0], tt_args[1], seconds)




'''

  mongodb

'''

# url, port, database and collection names
mongo_conf = ('localhost', 27017, 'twitter', tt_args[0])
client = pymongo.MongoClient(mongo_conf[0], mongo_conf[1])
db = client[mongo_conf[2]]
collection = db[mongo_conf[3]]

print 'storing...'

try:
  collection.insert_many(stts)
  print '[done] %d tweets stored in %s' % (collection.count(), collection.full_name)
except:
  print '[error]', sys.exc_info()[1]
  raise
finally:
  client.close()





print '[finished]'
