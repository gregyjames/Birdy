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

## Pick Graphs
By default all graphs are created in order to choose graphs go to prettyPrint.py, and comment out the function calls to the respective graphs.

- Follow_back();
  - Graph that shows how many of your followers you follow back.
- Default_profile();
  - Graph that shows how many of you Users have default profile images.
- User_Lang();
  - Pie chart of the various languages spoken by your audience.
- Tweet_Line();
  - Line graph of the last tweet time time of all your users. Allows you to zoom into specific time ranges.

## Contributing
At the end of the day every contribution is important regardless of size! Therefore, feel free to contribute to the project in any way that you can.
