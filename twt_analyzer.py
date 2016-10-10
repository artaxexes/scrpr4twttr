#!/usr/bin/python

import json



# load json file with tweets
tts = json.loads(open('tweets.json').read())


# filter(function, iterable)
# construct a list from those elements of iterable for which function returns true
was_rtt = filter(lambda tt: tt['retweeted'], tts["statuses"])


# map(function, iterable, ...)
# apply function to every item of iterable and return a list of the results
was_rtt_user = map(lambda tt: (tt['user'], tt['retweet_count']), was_rtt)


# get sum(rtt) by user
users = {}
for key, value in was_rtt_user:
  users[key] = users.get(key, 0) + value


# sort the result: more rtt first
users_sort = sorted(users, key = users.__getitem__, reverse = True)


# print the top 3 rtt users
print map(lambda x: x.encode('ascii'), users_sort[:3])
