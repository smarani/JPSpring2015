from django.http import HttpResponse
from xlrd import open_workbook,cellname
from foodpantry.models import FoodGroup, FoodItem, DateUploaded
from tweet import process
from django.utils import timezone

def handle_uploaded_file(f):
	book = open_workbook(file_contents=f.read())
	sheet = book.sheet_by_index(0)
	date = DateUploaded(date=timezone.now())
	date.save()

	cur_group = ''
	in_group = False
	total_sum = 0
	cur_group_Item = ''
	
	for row_index in range(sheet.nrows):
		if (sheet.cell(row_index, 0).value == ''):
			update_Group_Sum(cur_group_Item, total_sum)
			in_group = False
			cur_group = ''
			total_sum = 0
			g = ''
		elif in_group == False:
			cur_group = sheet.cell(row_index, 0).value
			opt_value_group = int(sheet.cell(row_index,1).value)
			in_group = True
			cur_group_Item = FoodGroup(name=cur_group, change = 0, deficit = 0, 
			optimal_number=opt_value_group, current_number= 0, upload_date=date)
			cur_group_Item.save()
		else:
			name = sheet.cell(row_index, 0).value
			current_value = int(sheet.cell(row_index, 1).value)
			opt_value = int(sheet.cell(row_index, 2).value)
			priority = sheet.cell(row_index, 3).value
			total_sum += current_value
			update_Item(name, cur_group_Item, opt_value, current_value, priority, date)
	update_Group_Sum(cur_group, total_sum)
	process()

def update_Item(name, food_group, optimal_number, current_number, priority, date):
	deficit = optimal_number - current_number
	
	try:
		date2 = DateUploaded.objects.all()[DateUploaded.objects.count()-2]
		recentfood = date2.fooditem_set.all()
		item = recentfood.get(name=name)
		change = current_number - item.current_number
		last_tweet = item.last_tweeted
	except:
		change = 0
		last_tweet = timezone.now().replace(year=1900)

	item = FoodItem(name=name, deficit = deficit, food_group = food_group, change = change, 
		optimal_number=optimal_number, current_number= current_number, priority=priority, upload_date=date, last_tweeted=last_tweet)
	item.save()

def update_Group_Sum(item, current_number):
	try:
		item.change = current_number - item.current_number
		item.deficit = item.optimal_number - item.current_number
		item.current_number = current_number
		item.save()
	except:
		pass