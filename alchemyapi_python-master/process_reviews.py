import pprint 
import cPickle as pickle

from alchemyapi import AlchemyAPI
alchemyapi = AlchemyAPI()


all_reviews = {}

with open('reviews.txt', 'rb') as dict_items_open:
	all_reviews = pickle.load(dict_items_open)

pp = pprint.PrettyPrinter(indent=4)

for key, data in all_reviews.iteritems():
	myText = data['text']
	response = alchemyapi.sentiment("text", myText)
	print "Sentiment: ", response["docSentiment"]["type"]