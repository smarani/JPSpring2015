from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UploadFileForm
from django.shortcuts import render_to_response
import tweepy
from django.contrib.auth.models import User
from django.contrib.auth import logout 
from django.contrib.auth import authenticate
from django.contrib.auth import login 
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.shortcuts import redirect
from django.utils import timezone
import datetime
from foodpantry.models import DateUploaded, FoodGroup, FoodItem, TweetSettings, Frequency, TweetOptions, Tweets, PastTweets, Drives
import excel_import as ex
import io
from somewhere import handle_uploaded_file
#from django.core.context_processors import csrf
from django.template import RequestContext
from table import reverseTable
from django.core.urlresolvers import reverse

CONSUMER_KEY = 'vj8qdrdUzHs5M05kom6UHDli5'
CONSUMER_SECRET = '9pguglaHVt9DDWgyEWSrcePpqkVnMOfOVwcokQZkATABbhOzBz'
ACCESS_TOKEN = '3065014882-Eq4hiZSchXnSbDzGLsyqhf7kiKlEmyP9AzBh7Pd'
ACCESS_TOKEN_SECRET = 'Y6srwfn7RxAawHcEScuMK6ciFD4ZYu7sIDWe9HHMh4KXv'
AUTH = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
AUTH.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(AUTH)

def signin(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('foodpantry:index'))
			else:
				return HttpResponse('Disabled Account')
		else:
			return HttpResponse('Invalid Login')
	else:
		return render(request, 'foodpantry/login.html')

def addtweettemplate(request):
	if request.POST['addordelete'] == 'add':		
		try:
			tweet = request.POST['tweetTemplate']
			category = request.POST['category']
			t = TweetOptions(upload_date=timezone.now(), tweet = tweet, category = category)
			t.save()
			return HttpResponse('worked!')
		except:
			return HttpResponse('error')
	elif request.POST['addordelete'] == 'delete':
		#return HttpResponse(len(request.POST['tweetTemplate']))
		try:
			tweet = request.POST['tweetTemplate'].strip()
			t = TweetOptions.objects.get(tweet = tweet.lstrip())
			t.delete()
			return HttpResponse('success')
		except:
			return HttpResponse('error')

def changesettings(request):
	if request.method == 'POST':
		deficit_hp = request.POST['deficit_hp']
		deficit_np = request.POST['deficit_np']
		deficit_lp = request.POST['deficit_lp']
		max_per_day = request.POST['max_per_day']
		change_for_thanks = request.POST['change_for_thanks']
		freq_lp = request.POST['freq_lp']
		freq_np = request.POST['freq_np']
		freq_hp = request.POST['freq_hp']
		#figure out how to read in checkboxes!!!
		t = TweetSettings(deficit_hp = deficit_hp, deficit_np = deficit_np, deficit_lp = deficit_lp, 
			max_per_day=max_per_day, change_for_thanks=change_for_thanks, upload_date=timezone.now(), freq_hp=freq_hp, 
			freq_np=freq_np, freq_lp=freq_lp)
		t.save()
		try:
			if request.POST['1week']:
				f = Frequency(number_of_days=7, category='before', settings=t)
				f.save()
		except:
			pass
		try:
			if request.POST['5days']:
				f = Frequency(number_of_days=5, category='before', settings=t)
				f.save()
		except:
			pass
		try:
			if request.POST['3days']:
				f = Frequency(number_of_days=3, category='before', settings=t)
				f.save()
		except:
			pass
		try:
			if request.POST['2days']:
				f = Frequency(number_of_days=2, category='before', settings=t)
				f.save()
		except:
			pass
		try:
			if request.POST['1day']:
				f = Frequency(number_of_days=1, category='before', settings=t)
				f.save()
		except:
			pass
		try:
			if request.POST['everyother']:
				f = Frequency(number_of_days=2, category='during', settings=t)
				f.save()
		except:
			pass
		try:
			if request.POST['every']:
				f = Frequency(number_of_days=1, category='during', settings=t)
				f.save()
		except:
			pass
		custom = request.POST['custom']
		if custom != '':
			f = Frequency(number_of_days=custom, category='before', settings=t)
			f.save()
	setting = TweetSettings.objects.all()[TweetSettings.objects.count() - 1]
	return render(request, 'foodpantry/settings.html', {'setting':setting, 'templates':TweetOptions.objects.all()})

def editsettings(request):
	setting = TweetSettings.objects.all()[TweetSettings.objects.count() - 1]
	return render(request, 'foodpantry/settings.html', {'setting':setting, 'templates':TweetOptions.objects.all()})

def drives(request):
	all_drives = Drives.objects.all()
	return render(request, 'foodpantry/drives.html', {'current_drives':all_drives})

def timetologout(request):
	logout(request)
	return render(request, 'foodpantry/login.html')

def adddrive(request):
	if request.method == 'POST':
		name = request.POST['driveName']
		location = request.POST['driveLocation']
		address = request.POST['driveAddress']
		start_date = datetime.datetime.strptime(request.POST['driveStartDate'], '%m/%d/%Y')
		end_date = datetime.datetime.strptime(request.POST['driveEndDate'], '%m/%d/%Y')
		duration = end_date-start_date
		notes = request.POST['specialNotes']
		thing = name+location+address+str(start_date)+str(duration.days)+notes
		d = Drives(name=name, location=location, address = address, start_date=start_date, duration=duration.days, notes=notes)
		d.save()
		returnValue = name+','+location+','+address+','+str(start_date)+','+str(duration.days)+notes
		return HttpResponse(returnValue)

def deletedrive(request):
	if request.method=='POST':
		d = Drives.objects.get(name=request.POST['driveName'].strip())
		d.delete()
		return HttpResponse('success')
	
def quicktweet(request):
	if request.method=='POST':

		api.update_status(status=request.POST['tweet'])
	return render(request, 'foodpantry/quicktweet.html')
	
def inventory(request):
	if not request.user.is_authenticated():
		return render(request, 'foodpantry/login.html')
	else:
		if request.method == 'POST':
			form = UploadFileForm(request.POST, request.FILES)
			if form.is_valid():
				handle_uploaded_file(request.FILES['file'])
		else:
			form = UploadFileForm()

		return render(request, 'foodpantry/test.html', {'rows':reverseTable()})

def index(request):
	#return render(request, 'foodpantry/home2.html')
	#return render(request, 'foodpantry/tabletest.html', {'rows':reverseTable()})
	if not request.user.is_authenticated():
		return render(request, 'foodpantry/login.html')
	else:
		return render(request, 'foodpantry/home2.html')

