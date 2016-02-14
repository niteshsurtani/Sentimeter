import pprint 
import cPickle as pickle
import requests
import json

marker = {1: 'negative', 2: 'negative', 3: 'neutral', 4: 'positive', 5: 'positive'}

with open('processed_reviews.txt', 'rb') as dict_items_open:
	all_reviews = pickle.load(dict_items_open)

count = 1
total = 190

alchemy_point = 0
aylien_point = 0
textalytics_point = 0

for k, data in all_reviews.iteritems():
	rating = int(data['rating'])
	rating_map = marker[rating]

	alchemy = data['alchemyapi']
	aylien = data['aylien']
	if('textalytics' in data):
		textalytics = data['textalytics']
	else:
		textalytics = 'none'

	if(alchemy == rating_map):
		alchemy_point += 1
	if(aylien == rating_map):
		aylien_point += 1
	if( textalytics == rating_map):
		textalytics_point += 1

	count = count + 1

print alchemy_point, aylien_point, textalytics_point
