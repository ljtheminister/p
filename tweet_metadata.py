import csv
import pymongo
from pymongo import MongoClient

import settings
import cPickle as pickle

import codecs

cnxn = MongoClient(settings.DATABASE_HOST)
db = cnxn[settings.DATABASE_NAME]
collection = db[settings.DATABASE_COLLECTION]

tweets = collection.find()

with codecs.open('metadata.txt', 'wb', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter='\t')
    for idx, tweet in enumerate(tweets[:5]):
	try:
	    #text = tweet['text'].decode('utf-8')
	    link = str(tweet['entities']['media'][0]['media_url'])
	    hashtags = [ht['text'] for ht in tweet['entities']['hashtags']]
	    geo = tweet['geo']
	    lang_tweet = tweet['lang']
	    lang_user = tweet['user']['lang'] 
	    tz_user = tweet['user']['time_zone']
	    '''
	    FIGURE OUT HOW TO USE UTF-8 ENCODING TO WRITE OUT TO TEXT FILE
	    writer.writerow((link, hashtags, lang_tweet, lang_user, tz_user))
	    '''
	except:
	    print idx
	    writer.writerow(())
