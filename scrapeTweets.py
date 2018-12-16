from flask import Flask, jsonify, request
from flask_cors import CORS # allow browser access
import bs4
import requests

# use $ FLASK_APP=scrapeTweets.py flask run

app = Flask(__name__)
CORS(app)

# <path:username> acts as a wildcard to get whatever is passed into the url
@app.route('/<path:username>')

def getTweet(username):
	# accepts a twitter profile name and returns 10 recent tweets

	# this will be returned
	tweets = []

	# get the page with requests module
	resSite = requests.get(f'https://twitter.com/{username}?lang=en')

	# parse page
	soup = bs4.BeautifulSoup(resSite.text, 'html.parser')

	# pull out all paragraphs with appropriate class
	text = soup.find_all('p', {'class': 'js-tweet-text'})

	# loop over tweets and add first ten to result
	for paragraph in text:
		if len(tweets) >= 10: break
		tweets.append(paragraph.text)

	return jsonify(tweets)

