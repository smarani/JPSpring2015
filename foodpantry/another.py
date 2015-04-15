from foodpantry.models import DateUploaded, FoodGroup, FoodItem, TweetSettings, Frequency, TweetOptions, Tweets, PastTweets, Drives
from django.utils import timezone
import datetime

def schedule():
	setting = TweetSettings.objects.all()[TweetSettings.objects.all().length - 1]

	deficit_hp = setting.deficit_hp
	deficit_np = setting.deficit_np
	deficit_lp = setting.deficit_lp

	frequencies = setting.Frequency.objects.all()
	freq_week_hp = frequencies.objects.get(category='high')
	freq_week_np = frequencies.objects.get(category='normal')
	freq_week_lp = frequencies.objects.get(category='low')
	freq_drives = frequencies.objects.get(category='drive')
	num_added = 0
	foodsToTweet = []

	high_priority = FoodItem.objects.get(priority='high')
	for item in high_priority:
		if item.deficit >= deficit_hp:
			if checkValid(item, freq_week_hp):
				foodsToTweet.append(item)
				num_added += 1
				if (num_added >= max_per_day): 
					break	

	if num_added < max_per_day:
		normal_priority = FoodItem.objects.get(priority='normal')
		for item in normal_priority:
			if item.deficit >= deficit_np:
				if checkValid(item, freq_week_np):
					foodsToTweet.append(item)
					num_added += 1	
					if (num_added >= max_per_day): 
						break			

	if num_added < max_per_day:
		low_priority = FoodItem.objects.get(priority='low')
		for item in low_priority:
			if item.deficit >= deficit_lp:
				if checkValid(item, freq_week_lp):
					foodsToTweet.append(item)
					num_added += 1
					if (num_added >= max_per_day): 
						break	

	makeTweets(foodsToTweet)
	driveTweet(freq_drives)

def makeTweets(foodsToTweet):
	foodTweets = TweetOptions.objects.get(category='food')
	i = 0
	for thing in foodsToTweet:
		t = Tweets(tweet = toTweet('food', foodTweets[i], thing))
		t.save()
		i += 1
		if (i == foodTweets.length-1):
			i=0

def driveTweet(freq):
	
	drive_freq = freq
	driveTweets = TweetOptions.objects.get(category='drive')

	i = 0
	for thing in Drives.objects.all():
		if checkValid(thing, drive_freq):
			t = Tweets(tweet = toTweet('drive', driveTweets[i], thing))
			t.save()
			i += 1
			if (i == driveTweets.length-1):
				i=0

def toTweet(itemType, default_string, food_item):
	if itemType == 'food':
		new_string = default_string.replace('*NAME*', food_item.name)
		new_string = new_string.replace('*DEFICIT*', food_item.deficit)
		new_string = new_string.replace('*PRIORITY*', food_item.priority)
		new_string = new_string.replace('*CURRENT_NUMBER*', food_item.current_number)
		new_string = new_string.replace('*OPTIMAL_NUMBER*', food_item.optimal_number)
	elif itemType == 'drive':
		new_string = default_string.replace('*NAME*', food_item.name)
		new_string = new_string.replace('*LOCATION*', food_item.location)
		new_string = new_string.replace("*STARTDATE*", food_item.start_date)
		new_string = new_string.replace('*DURATION*', food_item.duration)
	return new_string

def checkValid(item, freq_week):	
	last_tweet = item.last_tweeted
	difference = timezone.now() - last_tweet
	for thing in freq_week.objects.all():
		if difference.days() == thing.number_of_days:
			return True
	return False

