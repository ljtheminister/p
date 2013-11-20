'''
Created on Feb 25, 2013

@author: mohamed
'''
import pymongo


def initialize_database(host, database, collection):
    connection = pymongo.MongoClient(host, safe=True)
    print connection
    
    # get a handle to the database
    database = connection[database]
    print database
    
    collection = database[collection]
    print collection 
    
    return collection