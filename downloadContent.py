'''
Created November 21, 2013
@JohnMin
'''

import pymongo
from pymongo import MongoClient

import settings
import pickle

cnxn = MongoClient(settings.DATABASE_HOST)
db = cnxn[settings.DATABASE_NAME]
collection = db[settings.DATABASE_COLLECTION]
print 'connected to Mongo'

list_urls = []
bad_tweets = []

#list_urls = [str(tweet[u'entities'][u'media'][0][u'media_url_https']) for tweet in collection.find()]

for tweet in collection.find():
    try:
	entity_dict = tweet[u'entities']
	media_dict = entity_dict[u'media'][0]
	media_url = str(media_dict[u'media_url_https'])
	list_urls.append(media_url)
	    
    except:
	bad_tweets.append(tweet)
	print 'Sum Ting Wong'

pickle.dump(list_urls, open('url_list.p', 'wb'))
pickle.dump(bad_tweets, open('bad_tweetes.p', 'wb'))
