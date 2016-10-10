#!/usr/bin/python

import json

twts = json.loads(open('tweets.json').read())
print(map(lambda x: 1 if x["retweeted"] else 0, tweets["statuses"]))
