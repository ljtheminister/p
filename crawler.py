# coding=utf-8
import sys
import json
import traceback

import tweepy
import settings

import databaseConnection

#This is the over-ridding of the Tweepy twitter stream listener
class TwitterStreamListener(tweepy.streaming.StreamListener):

    def on_data(self, data):

        data = json.loads(data)

        if ('entities' in data and 'media' in data['entities'] and 'type' in data['entities']['media'][0] and data['entities']['media'][0]['type'] == 'photo') or (data['source'] == '<a href=\"http://vine.co\" rel=\"nofollow\">Vine - Make a Scene</a>'):
            collection.save(data)
            print collection.count()


def load_hashtags():

    hashtags = list()

    #file = open("hashtags")
    file = open("hashtags_english")
    #file = open("hashtags_arabic")
    for line in file:
        line = line.strip()

        hashtags.append(line)

    return hashtags

if __name__ == '__main__' :

    while True:
	try:

	    print 'Loading hashtags.'
	    hashtags = load_hashtags()
	    print 'Hashtags loaded.'

	    print 'Connecting to databse..'
	    collection = databaseConnection.initialize_database(settings.DATABASE_HOST, settings.DATABASE_NAME, settings.DATABASE_COLLECTION)
	    print 'Connected to databse.'

	    print 'Connecting to the Twitter Stream...'
	    #Initialize a TwitterStreamListener that inherits from StreamListener
	    tsl = TwitterStreamListener()

	    #set the authentication
	    auth = tweepy.OAuthHandler(settings.TWITTER_CONSUMER_KEY, settings.TWITTER_CONSUMER_SECRET)
	    auth.set_access_token(settings.TWITTER_ACCESS_TOKEN, settings.TWITTER_ACCESS_TOKEN_SECRET)

	    print 'Connected to the Twitter Stream.'

	    #start listening to the stream
	    stream = tweepy.Stream(auth, tsl)

	    print 'stream authorized'
	    #set the track keyword to listen on
	    stream.filter(track=hashtags)
	    print 'stream is filtering hashtags'

	except Exception as e:
	    print 'Exception'
	    for frame in traceback.extract_tb(sys.exc_info()[2]):
		fname, lineno, fn, text = frame
		print fname + ':' + __name__ + ':' + str(lineno) + ':' + text + ':' + e.message

	    if stream is not None:
		print 'stream is not None'
		stream.disconnect()
