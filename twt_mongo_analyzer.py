#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import pymongo
from bson.code import Code





'''

  mongodb

'''

# url, port, database and collection names
mongo_conf = ('localhost', 27017, 'twitter', 'tweets')
client = pymongo.MongoClient(mongo_conf[0], mongo_conf[1])
db = client[mongo_conf[2]]
collection = db[mongo_conf[3]]

print 'doing mongodb aggregate...'

try:
  collection.aggregate(
    [
      {"$match": {"retweet_count":{"$gte":1}}},
      {"$group": {"_id":"$user.screen_name","retweeted":{"$sum":"$retweet_count"}}},
      {"$sort": {"retweeted":-1}},
      {"$out":"aggregate"}
    ]
  )
  print '[done] aggregate result:', db['aggregate'].count(), 'users had retweeted tweet'
except:
  print '[error]', sys.exc_info()[1]
  raise
finally:
  client.close

print 'doing mongodb map reduce...'

try:
  mapper = Code(
  '''
  function(){
      emit(this.user.screen_name, this.retweet_count);
    }
  '''
  )
  reducer = Code(
  '''
    function(key, values){
      return Array.sum(values);
    }
  '''
  )
  collection.map_reduce(mapper, reducer, 'mapreduce', query = {'retweet_count':{'$gte':1}})
  print '[done] map reduce result:', db['mapreduce'].count(), 'users had retweeted tweet'
except:
  print '[error]', sys.exc_info()[1]
  raise
finally:
  client.close


top = 10
print 'top', top, 'retweeted users'
for user in db['aggregate'].find(limit = top):
  print '*', user['_id'], 'retweeted', user['retweeted'], 'times'

print 'finished'
