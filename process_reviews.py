import pprint 
import cPickle as pickle
import requests
import json
import apis.aylienapi.aylienapiclient.textapi
import apis.alchemyapi.alchemyapi

def processReviews():
	mapping = {'N' : 'negative', 'P': 'positive', 'NEU':'neutral', 'NONE':'none'}

	# ALCHEMY
	alchemyapi = apis.alchemyapi.alchemyapi.AlchemyAPI()

	# AYLIEN
	c = apis.aylienapi.aylienapiclient.textapi.Client("4df6473c", "f827888e31b6b52f85a6061eb3f18ad1")

	# Textalytics
	api = 'http://api.meaningcloud.com/sentiment-2.0'
	key = '6c46872fd5bded758034d0e5c6d1cf00'
	model = 'general_es' # general_es / general_es / general_fr


	all_reviews = {}

	with open('storage.tmp/reviews.txt', 'rb') as dict_items_open:
		all_reviews = pickle.load(dict_items_open)

	pp = pprint.PrettyPrinter(indent=4)


	count = 1 
	for k, data in all_reviews.iteritems():
		print count
		myText = data['text'].encode('utf-8')

		# Alchemy API
		response = alchemyapi.sentiment("text", myText)
		data['alchemyapi'] = response["docSentiment"]["type"]

		# Textalytics
		parameters = {'key': key,'model': model, 'txt': myText, 'src': 'sdk-python-2.0'}
		r = requests.post(api, params=parameters)
		response = r.content
		response_json = json.loads(response)

		try:
			if response_json['score_tag'] != '':
				data['textalytics'] =  mapping[response_json['score_tag']]
		
		except KeyError:
			print "Not found"

		# AYLIEN
		s = c.Sentiment({'text': myText})
		data['aylien'] = s['polarity']
		count = count+1

	with open('storage.tmp/processed_reviews.txt', 'wb') as dict_items_save:
		pickle.dump(all_reviews, dict_items_save)