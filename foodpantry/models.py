from django.db import models
from django.utils import timezone

class DateUploaded(models.Model):
    date = models.DateTimeField('date published', default=timezone.now)

class FoodGroup(models.Model):
    upload_date = models.ForeignKey(DateUploaded)
    name = models.CharField(max_length=200)
    optimal_number = models.IntegerField(default=0)
    current_number = models.IntegerField(default=0)
    change = models.IntegerField(default=0)
    deficit = models.IntegerField(default=0)
    priority = models.CharField(max_length=100, default=' ')
    def __str__(self):              
        return self.name                

class FoodItem(models.Model):
    upload_date = models.ForeignKey(DateUploaded)
    food_group = models.ForeignKey(FoodGroup)
    name = models.CharField(max_length=200)
    optimal_number = models.IntegerField(default=0)
    current_number = models.IntegerField(default=0)
    change = models.IntegerField(default=0)
    deficit = models.IntegerField(default=0)
    priority = models.CharField(max_length=200, default='low')
    last_tweeted = models.DateTimeField('last tweet', default=timezone.now().replace(year=1900))
    def __str__(self):              
        return self.name

class TweetSettings(models.Model):
    upload_date = models.DateTimeField('date published', default=timezone.now)

    deficit_hp = models.IntegerField(default=0)
    deficit_np = models.IntegerField(default=0)
    deficit_lp = models.IntegerField(default=0)

    freq_hp = models.IntegerField(default=0)
    freq_np = models.IntegerField(default=0)
    freq_lp = models.IntegerField(default=0)

    max_per_day = models.IntegerField(default=0)

    change_for_thanks = models.CharField(max_length=50)

class Frequency(models.Model):
    number_of_days = models.IntegerField(default=0)
    category = models.CharField(max_length=100)
    settings = models.ForeignKey(TweetSettings)

class TweetOptions(models.Model):
    upload_date = models.DateTimeField('date published', default=timezone.now)
    tweet = models.CharField(max_length=140)
    #food or drive
    category = models.CharField(max_length=50)

class Tweets(models.Model):
    tweet = models.CharField(max_length=140)

class PastTweets(models.Model):
    tweet = models.CharField(max_length=140)
    date = models.DateTimeField('date published', default=timezone.now)

class Drives(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    start_date = models.DateTimeField('Drive Date')
    duration = models.IntegerField(default=0)
    notes = models.CharField(max_length=200)
    last_tweeted = models.DateTimeField('last tweet', default=timezone.now().replace(year=1900))
    created_on = models.DateTimeField('date published', default=timezone.now)
