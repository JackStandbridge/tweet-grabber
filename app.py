from flask import Flask, jsonify, request
from flask_cors import CORS # allow browser access
import bs4
import requests

# use $ FLASK_APP={filename}.py flask run or just $flask run if the target file is called app.py

app = Flask(__name__)
CORS(app)

# <path:username> acts as a wildcard to get whatever is passed into the url
@app.route('/<path:username>')

def getTweets(username):
	# accepts a twitter profile name and returns 10 recent tweets

	# this will be returned
	result = []

	# get the page with requests module
	siteText = requests.get(f'https://twitter.com/{username}?lang=en').text

	# parse page
	soup = bs4.BeautifulSoup(siteText, 'html.parser')

	# pull out all tweets with appropriate class
	tweets = soup.find_all('div', {'class': 'original-tweet'})

	# loop over tweets and add first ten to result
	for tweet in tweets:
		if len(result) >= 10: break

		tweetComponents = {}

		tweetComponents['author'] = tweet.find('strong', {'class': 'fullname'}).text
		tweetComponents['time'] = tweet.find('span', {'class': '_timestamp'}).text
		tweetComponents['body'] = tweet.find('p', {'class': 'tweet-text'}).text

		result.append(tweetComponents)

	return jsonify(result)
