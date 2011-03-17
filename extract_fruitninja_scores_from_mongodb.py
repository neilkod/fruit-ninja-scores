def fruitninja_tweets():
	tweets = create_connection(False)
	regexp = re.compile('^I.*fruitninja.com')
	cur = tweets.conftweets.find({'text': regexp}, {'text': 1,'created_at':1,'user':1})
	itr = 0
	for item in cur:
		try:
			txt = '\t'.join ([item['created_at'], item['user']['screen_name'], item['text']])
			print txt
			itr += 1
		except:
			pass
	return itr