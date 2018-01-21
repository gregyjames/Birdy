[![Build Status](https://travis-ci.com/gregyjames/Birdy.svg?token=TAMu6qDfByKbi2gkRs9d&branch=master)](https://travis-ci.com/gregyjames/Birdy)

# Birdy
Birdy is a simple tool to analyze key data about your twitter following/followers.

## Libraries Used
1. [Tweepy](https://github.com/tweepy/tweepy)
2. [TinyDB](https://github.com/msiemens/tinydb)
3. [Progressbar](https://pypi.python.org/pypi/progressbar2)
4. [Plotly](https://plot.ly/python/)

## Setup
In order to use the tools you need to have Twitter Api app registered. If you are confused on how to do so follow the guide [here](https://iag.me/socialmedia/how-to-create-a-twitter-app-in-8-easy-steps/). After you do so, create a file called config.ini and configure it like so with the data from the Twitter API page:

```
[API_KEYS]
consumer_key = consumer_key_no_qoutes
consumer_secret = consumer_secret_no_qoutes
access_token = access_token_no_qoutes
access_token_secret = access_token_secret_no_qoutes
```

## Running
1. pip install -r requirements.txt
2. python main.py

## Contributing
At the end of the day every contribution is important regardless of size! Therefore, feel free to contribute to the project in any way that you can.
