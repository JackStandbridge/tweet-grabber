# Tweet-Grabber

A little site that displays the first ten tweets for a given twitter account name.

Uses python to scrape the page for tweets, then adds them to an html page with vanilla javascript.

Built with python 3, but may work with python 2, not tested. Python script requires flask, flask_cors, beautifulsoup4 and requests modules. Install python 3, then run:

$ pip3 install Flask Flask-Cors beautifulsoup4 requests

Navigate to project directory and then run:

$ flask run

Server will run on http://127.0.0.1:5000/

Expect no output at that uri because there is no route for it. Instead, append a twitter username to it to see the raw output.

main.js will make get requests to the address based on the input in the form field upon submitting, and fill in the twitter username in the url to make the request.
