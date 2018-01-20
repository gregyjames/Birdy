from tinydb import TinyDB, Query
import tweepy
import time
import progressbar
from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('config.ini')

consumer_key =  parser.get('API_KEYS', 'consumer_key')
consumer_secret = parser.get('API_KEYS', 'consumer_secret')
access_token = parser.get('API_KEYS', 'access_token')
access_token_secret = parser.get('API_KEYS', 'access_token_secret')

auth = tweepy.OAuthHandler(consumer_key , consumer_secret)
auth.set_access_token(access_token, access_token_secret)
db = TinyDB('db.json')
db.purge()
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

friends = api.followers_ids()

count = 0;

bar = progressbar.ProgressBar(redirect_stdout=True, max_value=len(friends))
for id in friends:
    user = api.get_user(id)
    db.insert({'id': user.id, 'location': user.location, 'followers_count': user.followers_count, 'statuses_count': user.statuses_count, 'friends_count': user.friends_count, 'screen_name': user.screen_name, 'lang': user.lang, 'following': user.following, 'time_zone':user.time_zone, 'created_at': user.created_at, 'default_user': user.default_profile, 'default_profile_image': user.default_profile_image})
    count = count + 1
    time.sleep(0.1)
    bar.update(count)

