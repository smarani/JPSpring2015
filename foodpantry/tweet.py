import tweepy
from foodpantry.models import DateUploaded, FoodGroup, FoodItem, TweetSettings, Frequency, TweetOptions, Tweets, PastTweets, Drives
from django.utils import timezone
import datetime


CONSUMER_KEY = 'vj8qdrdUzHs5M05kom6UHDli5'
CONSUMER_SECRET = '9pguglaHVt9DDWgyEWSrcePpqkVnMOfOVwcokQZkATABbhOzBz'
ACCESS_TOKEN = '3065014882-Eq4hiZSchXnSbDzGLsyqhf7kiKlEmyP9AzBh7Pd'
ACCESS_TOKEN_SECRET = 'Y6srwfn7RxAawHcEScuMK6ciFD4ZYu7sIDWe9HHMh4KXv'
AUTH = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
AUTH.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(AUTH)

def process():
	date = DateUploaded.objects.all()[DateUploaded.objects.count()-1]
	items = date.fooditem_set.all()

	setting = TweetSettings.objects.all()[TweetSettings.objects.count() - 1]
	change_needed = setting.change_for_thanks
	thankyous = []

	if change_needed == 'any':
		for thing in items:
			if thing.change > 0:
				thankyous.append(thing)
	elif change_needed == 'surplus':
		for thing in items:
			if (thing.change > 0) & (thing.deficit < 0):
				thankyous.append(thing)
	elif change_needed == 'reached':
		for thing in items:
			if (thing.change > 0) & (thing.deficit == 0):
				thankyous.append(thing)
	tweetThanks(thankyous)

def tweetThanks(item):
	driveTweets = TweetOptions.objects.filter(category='thanks')
	i = 0
	for thing in item:
		status = driveTweets[i].tweet.replace('*FOOD*', thing.name)
		api.update_status(status=status)
		i+=1
		if (i >= driveTweets.count()):
			i = 0

def schedule():
	setting = TweetSettings.objects.all()[TweetSettings.objects.count() - 1]

	deficit_hp = setting.deficit_hp
	deficit_np = setting.deficit_np
	deficit_lp = setting.deficit_lp

	freq_week_hp = setting.freq_hp
	freq_week_np = setting.freq_np
	freq_week_lp = setting.freq_lp
	freq_drives_before = setting.frequency_set.filter(category='before')
	freq_drives_during = setting.frequency_set.filter(category='during')

	max_per_day = setting.max_per_day
	num_added = 0
	foodsToTweet = []

	date = DateUploaded.objects.all()[DateUploaded.objects.count()-1]
	recent_food = date.fooditem_set.all()

	high_priority = recent_food.filter(priority='high')
	for item in high_priority:
		if item.deficit >= deficit_hp:
			if checkValid(item, freq_week_hp):
				foodsToTweet.append(item)
				num_added += 1
				if (num_added >= max_per_day): 
					break	

	if num_added < max_per_day:
		normal_priority = recent_food.filter(priority='normal')
		for item in normal_priority:
			if item.deficit >= deficit_np:
				if checkValid(item, freq_week_np):
					foodsToTweet.append(item)
					num_added += 1	
					if (num_added >= max_per_day): 
						break			

	if num_added < max_per_day:
		low_priority = recent_food.filter(priority='low')
		for item in low_priority:
			if item.deficit >= deficit_lp:
				if checkValid(item, freq_week_lp):
					foodsToTweet.append(item)
					num_added += 1
					if (num_added >= max_per_day): 
						break	

	makeTweets(foodsToTweet)
	driveTweet(freq_drives_before, freq_drives_during)

def makeTweets(foodsToTweet):
	foodTweets = TweetOptions.objects.filter(category='food')
	i = 0
	for thing in foodsToTweet:
		twee = toTweet('food', foodTweets[i].tweet, thing)
		t = Tweets(tweet=twee)
		t.save()
		thing.last_tweeted = timezone.now()
		thing.save()
		i += 1
		if (i >= foodTweets.count()-1):
			i=0

def driveTweet(freq_before, freq_during):	
	driveTweets = TweetOptions.objects.filter(category='drive')
	i = 0
	for thing in Drives.objects.all():
		if checkValidDrive(thing, freq_before, freq_during):
			twee = toTweet('drive', driveTweets[i].tweet, thing)
			t = Tweets(tweet = twee)
			t.save()
			thing.last_tweeted = timezone.now()
			thing.save()
			i += 1
			if (i == driveTweets.count()-1):
				i=0

def toTweet(itemType, default_string, food_item):
	if itemType == 'food':
		new_string = default_string.replace('*NAME*', food_item.name)
		new_string = new_string.replace('*DEFICIT*', str(food_item.deficit))
		new_string = new_string.replace('*PRIORITY*', str(food_item.priority))
		new_string = new_string.replace('*CURRENT_NUMBER*', str(food_item.current_number))
		new_string = new_string.replace('*OPTIMAL_NUMBER*', str(food_item.optimal_number))
	elif itemType == 'drive':
		new_string = default_string.replace('*NAME*', food_item.name)
		new_string = new_string.replace('*LOCATION*', str(food_item.location))
		new_string = new_string.replace('*ADDRESS*', str(food_item.address))
		new_string = new_string.replace("*STARTDATE*", str(food_item.start_date))
		new_string = new_string.replace('*DURATION*', str(food_item.duration))
	return new_string

def checkValidDrive(item, freq_week_before, freq_week_during):	
	last_tweet = item.last_tweeted
	difference = timezone.now() - last_tweet
	in_drive = timezone.now()-item.start_date
	if in_drive.days > item.duration:
		item.delete()
	if in_drive.days > 0:
		for thing in freq_week_during:
			if difference.days == thing.number_of_days:
				return True
	if abs(difference.days) > 365:
		return True
	for thing in freq_week_before:
		if abs(difference.days) == thing.number_of_days:
			return True
	return False

def checkValid(item, freq_week):	
	last_tweet = item.last_tweeted
	difference = timezone.now() - last_tweet
	if abs(difference.days) > 365:
		return True
	if abs(difference.days) == freq_week:
		return True
	return False








