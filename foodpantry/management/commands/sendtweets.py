from django.core.management.base import BaseCommand, CommandError
import tweepy
from foodpantry.models import Tweets, PastTweets
from foodpantry.tweet import schedule
from django.utils import timezone
import requests.packages.urllib3.contrib.pyopenssl
requests.packages.urllib3.contrib.pyopenssl.inject_into_urllib3()

CONSUMER_KEY = 'vj8qdrdUzHs5M05kom6UHDli5'
CONSUMER_SECRET = '9pguglaHVt9DDWgyEWSrcePpqkVnMOfOVwcokQZkATABbhOzBz'
ACCESS_TOKEN = '3065014882-Eq4hiZSchXnSbDzGLsyqhf7kiKlEmyP9AzBh7Pd'
ACCESS_TOKEN_SECRET = 'Y6srwfn7RxAawHcEScuMK6ciFD4ZYu7sIDWe9HHMh4KXv'
AUTH = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
AUTH.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(AUTH)

class Command(BaseCommand):
	def handle(self, *args, **options):
		try:
			schedule()
			t = Tweets.objects.all()
			for thing in t:
				api.update_status(status=thing.tweet)
				history = PastTweets(tweet=thing.tweet, date=timezone.now())
				history.save()
				thing.delete()
		except:
			print 'error!'