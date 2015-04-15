import time
import tweepy
from foodpantry.models import FoodGroup, FoodItem


CONSUMER_KEY = 'vj8qdrdUzHs5M05kom6UHDli5'
CONSUMER_SECRET = '9pguglaHVt9DDWgyEWSrcePpqkVnMOfOVwcokQZkATABbhOzBz'
ACCESS_TOKEN = '3065014882-Eq4hiZSchXnSbDzGLsyqhf7kiKlEmyP9AzBh7Pd'
ACCESS_TOKEN_SECRET = 'Y6srwfn7RxAawHcEScuMK6ciFD4ZYu7sIDWe9HHMh4KXv'
AUTH = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
AUTH.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(AUTH)

def scheduler():
	count = 0
	while (True): 
		thing = "This is tweet" + str(count)
		api.update_status(status=thing)
		time.sleep(300)
		count += 1