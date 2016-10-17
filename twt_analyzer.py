#!/usr/bin/python

import sys
import pymongo
from bson.code import Code

# config mongodb connection: mongodb url, port, database and collection names
mongo_conf = ('localhost', 27017, 'twitter', 'tweets')
client = pymongo.MongoClient(mongo_conf[0], mongo_conf[1])
db = client[mongo_conf[2]]
collection = db[mongo_conf[3]]


# aggregate
print 'doing aggregate...',
try:
  collection.aggregate(
    [
      {"$match": {"retweet_count":{"$gt":1}}},
      {"$group": {"_id":"$user.screen_name","retweeted":{"$sum":"$retweet_count"}}},
      #{"$sort": {"retweeted":-1}},
      {"$out":"aggregate"}
    ]
  )
  print '\t[done] aggregate result:', db['aggregate'].count(), 'users'
  print '\ttop 5 retweeted users'
  for user in db['aggregate'].find(limit = 5).sort([('retweeted', pymongo.DESCENDING)]):
    print '\t *', user['_id'], 'retweeted', user['retweeted'], 'times'
except:
  print '\t[error]', sys.exc_info()[1]
  raise


# map reduce
print '\ndoing map reduce...',
try:
  mapper = Code('function(){ emit(this.user.screen_name, this.retweet_count); }')
  reducer = Code('function(key, values){ return Array.sum(values); }')
  collection.map_reduce(mapper, reducer, 'mapreduce', query = {'retweet_count':{'$gt':1}})
  print '\t[done] map reduce result:', db['mapreduce'].count(), 'users'
  print '\ttop 5 retweeted users'
  for user in db['mapreduce'].find(limit = 5).sort([('value', pymongo.DESCENDING)]):
    print '\t *', user['_id'], 'retweeted', int(user['value']), 'times'
except:
  print '\t[error]', sys.exc_info()[1]
  raise
finally:
  client.close

print 'finished'
