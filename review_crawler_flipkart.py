import cPickle as pickle
import requests
import os
from bs4 import BeautifulSoup
import pprint 
import json
import re



def getReviews(page, count):
	content = requests.get(page)
	html = content.text
	soup = BeautifulSoup(html)
	reviews = {}
	total = 1

	for level1 in soup.find_all("div", {'class': 'review-list'}):
		for level2 in level1("div", {'class': 'fclear fk-review fk-position-relative line '}):

			review = {}

			for level3 in level2("div", {'class': 'unit size1of5 section1'}):
				for level4 in level3("div", {'class': 'line'}):
					for level5 in level4("div", {'class': 'fk-stars'}):
						review['rating'] = level5['title'].split()[0]

			for level3 in level2("div", {'class': 'lastUnit size4of5 section2'}):
				for level4 in level3("div", {'class': 'line fk-font-normal bmargin5 dark-gray'}):
					title = str(level4("strong")[0])

					title = re.sub(r"<.*>", "", title)
					review['title'] = title.strip()
					# print review['title']

				for level4 in level3("p", {'class': 'line bmargin10'}):
					for level5 in level4("span", {'class': 'review-text'}):
						text = re.sub(r"<.*>", "", level5.text)
						review['text'] = text.strip()

			reviews[total + count] = review
			total = total + 1
	return reviews, total


def extractReviews():
	all_reviews = {}
	total = 1
	count = 0
	pp = pprint.PrettyPrinter(indent=4)

	while(count < 200):
		page = "http://www.flipkart.com/moto-g-3rd-generation/product-reviews/ITME9YSJR7MFRY3N?pid=MOBE6KK93JG5WKB2&rating=1,2,3,4,5&reviewers=all&type=all&sort=most_helpful&start=" + str(count)
		reviews, total = getReviews(page, count)

		for k,d in reviews.iteritems():
			all_reviews[k] = d
		count = count + 10


	with open('storage.tmp/reviews.txt', 'wb') as dict_items_save:
		pickle.dump(all_reviews, dict_items_save)