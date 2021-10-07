import tweepy as tp
from tweepy.auth import AuthHandler

API_KEY = 'NRsqOU5e4r5ZCknOfsdOC2hPt'
API_SECRET = '2zIqdoVrDSRUc8QD4cG9ScDe4OxxOcMZOCBm0RbGPGpUnUpdhk'
ACCESS_TOKEN = '1440589525424623629-NQx6rIj1RavoBayKm3qfK63JUPzbjT'
ACCESS_SECRET = 'IGtvwgOntpd2xSXMui2jmxOqk3pLdvQA9G9LzFEh7XHDnh'

auth = tp.AuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tp.API(auth)

tweets = api.search(q='johnny depp')

for tweet in tweets:
    print(tweet)
    break
