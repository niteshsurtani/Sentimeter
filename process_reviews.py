import pprint 
import cPickle as pickle
import requests
import json

from alchemyapi import AlchemyAPI
alchemyapi = AlchemyAPI()

all_reviews = {}

with open('reviews.txt', 'rb') as dict_items_open:
	all_reviews = pickle.load(dict_items_open)

pp = pprint.PrettyPrinter(indent=4)

for key, data in all_reviews.iteritems():
	myText = data['text']

	Alchemy API
	response = alchemyapi.sentiment("text", myText)
	print "Sentiment: ", response["docSentiment"]["type"]

	# Textalytics
	# api = 'http://api.meaningcloud.com/sentiment-2.0'
	# key = '6c46872fd5bded758034d0e5c6d1cf00'
	# model = 'general_es' # general_es / general_es / general_fr

	# parameters = {'key': key,'model': model, 'txt': myText, 'src': 'sdk-python-2.0'}
	# print myText
	# r = requests.post(api, params=parameters)
	# print "Here"
	# response = r.content
	# response_json = json.loads(response)
	# print response

	# try:
	# 	if response_json['score_tag'] != '':
	# 		print 'Global sentiment: ' + response_json['score_tag'] +' (' + response_json['agreement'] + ')'
	
	# except KeyError:
	# 	print "Not found"

	