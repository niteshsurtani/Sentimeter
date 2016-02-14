# -*- encoding: utf-8 -*-
"""
 Sentiment Analysis 2.0 starting client for Python.

 In order to run this example, the license key must be included in the key variable.
 If you don't know your key, check your personal area at MeaningCloud (https://www.meaningcloud.com/developer/account/licenses)

 Once you have the key, edit the parameters and call "python sentimentclient-2.0.py"

 You can find more information at http://www.meaningcloud.com/developer/sentiment-analysis/doc/2.0

 @author     MeaningCloud
 @contact    http://www.meaningcloud.com 
 @copyright  Copyright (c) 2015, MeaningCloud LLC All rights reserved.
"""

import requests
import json

txt = 

# We define the variables need to call the API
api = 'http://api.meaningcloud.com/sentiment-2.0'
key = '6c46872fd5bded758034d0e5c6d1cf00'
model = 'general_es' # general_es / general_es / general_fr

# We make the request and parse the response
parameters = {'key': key,'model': model, 'txt': txt, 'src': 'sdk-python-2.0'}
r = requests.post(api, params=parameters)
response = r.content
response_json = json.loads(response)

# Show the response
print "Response"
print "================="
print response
print "\n"

# Prints the global sentiment values
print "Sentiment: "
print "==========="

try:
  if response_json['score_tag'] != '':
    print 'Global sentiment: ' + response_json['score_tag'] +' (' + response_json['agreement'] + ')'
    print 'Subjectivity: ' + response_json['subjectivity']
    print 'Irony: ' + response_json['irony']
    print 'Confidence: ' + response_json['confidence']
  else:
    print "Not found"
except KeyError:
  print "Not found"

try:
  if len(response_json['sentimented_entity_list']) > 0:
    print "\nEntities"
    print "==========="
    entities = response_json['sentimented_entity_list']
    for index in range(len(entities)):
      output = ''
      output += ' - ' + entities[index]['form']
      try:
        output += ' (' + entities[index]['type'] + ')'
      except KeyError:
        pass
      print output
except KeyError:
  pass

try:
  if len(response_json['sentimented_concept_list']) > 0:
    print "\nConcepts"
    print "==========="
    concepts = response_json['sentimented_concept_list']
    for index in range(len(concepts)):
      output = ''
      output += ' - ' + concepts[index]['form']
      try:
        output += ' (' + concepts[index]['type'] + ')'
      except KeyError:
        pass
      print output
except KeyError:
  pass

print "\n"
