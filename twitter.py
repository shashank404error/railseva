import tweepy
import oauth2 as oauth
import requests
import config

APIKey = config.twitter_config["APIKey"]
APIKeySecret = config.twitter_config["APIKeySecret"]
AccessToken = config.twitter_config["AccessToken"]
AcceessTokenSecret = config.twitter_config["AcceessTokenSecret"]

def twitter_api():
    consumer_key = APIKey
    consumer_secret = APIKeySecret
    access_token = AccessToken
    access_token_secret = AcceessTokenSecret
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")
    return api

def tweet(message):
    api = twitter_api()
    resp = api.update_status(message)
    #tweet = api.get_status(id_of_tweet)
    #print(tweet)
    print(resp._json["id_str"])
    return resp._json["id_str"]