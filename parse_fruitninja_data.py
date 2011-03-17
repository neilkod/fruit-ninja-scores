#!/bin/python

import sys, re
sliced_regexp = re.compile('sliced (\d{1,8})')
scored_regexp = re.compile('scored (\d{1,8}) points')
with_regexp = re.compile('with (.*)!')
including_regexp = re.compile('including (.*) on')
device_regexp = re.compile('(iP.*?)[,!]')
for line in sys.stdin:
	try:
		with_text = ''
		device_text = ''
		including_text = ''
		data = line.strip()
		(created_at, username, text) = data.split('\t')
		# now, separate the types of 'scores' posted
		# the tweets contain either scores if they were playing in
		# arcade mode or zen mode
		# or if they were playing in regular mode(?) then
		# the score is the count of items sliced
		if 'scored' in text:
			# do stuff here
			score_match = scored_regexp.search(text)
			score = score_match.groups()[0]
			method = 'scored'
		elif 'sliced' in text:
			sliced_match = sliced_regexp.search(text)
			score =  sliced_match.groups()[0]
			method = 'sliced'
		if 'with' in text:
			with_text = with_regexp.search(text).groups()[0]
		if 'including' in text:
			including_text = including_regexp.search(text).groups()[0]
		else:
			pass
		try:
			device_text = device_regexp.search(text).groups()[0]
		except:
			device = ''
		output = '\t'.join([created_at,username,method,score,device_text,with_text,including_text])
		print output
	except:
		# likely bad data
		pass	