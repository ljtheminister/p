import csv
import pymongo
from pymongo import MongoClient

import settings
import cPickle as pickle
import codecs
from collections import defaultdict

cnxn = MongoClient(settings.DATABASE_HOST)
db = cnxn[settings.DATABASE_NAME]
collection = db[settings.DATABASE_COLLECTION]

tweets = collection.find()

suspended_accts = defaultdict(int)
visited_urls = defaultdict(int)
visited_urls_expanded = defaultdict(int)

suspended_accts['tawtheq'] += 1
suspended_accts['3lanKsa'] += 1
suspended_accts['mikandynothem'] += 1

#with codecs.open('metadata.txt', 'wb', encoding='utf-8') as f:
with open('tweet_metadata.txt', 'wb') as f:
    writer = csv.writer(f, delimiter='\t')
    for idx, tweet in enumerate(tweets):
	try:
	    #text = tweet['text'].decode('utf-8')
	    link = str(tweet['entities']['media'][0]['media_url'])
	    link_long = str(tweet['entities']['media'][0]['expanded_url'])
	    #hashtags = [ht['text'] for ht in tweet['entities']['hashtags']]
	    retweeted = tweet['retweeted']
	    geo = tweet['geo']
	    lang_tweet = tweet['lang']
	    lang_user = tweet['user']['lang'] 
	    tz_user = tweet['user']['time_zone']
	    user_handle = tweet['user']['screen_name']

	    visited = False
	    visited_long = False
	    suspended = False

	    if visited_urls[link]:
		visited = True
	    visited_urls[link] += 1

	    if visited_urls_expanded[link_long]:
		visited_long = True
	    visited_urls_expanded[link_long] 

	    if suspended_accts[user_handle]:
		suspended = True

	    writer.writerow((idx, link_long, user_handle, visited, visited_long, suspended, retweeted, geo, lang_tweet, lang_user, tz_user))
	except:
	    print idx
	    writer.writerow(())
