import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
# Uncomment below for Django 1.7 +
#import django
#django.setup()

from xlrd import open_workbook,cellname
from foodpantry.models import FoodGroup, FoodItem

def ProcessExcel(filename):
	g = FoodGroup(name='Fruits')
	g.save()
	book = open_workbook(filename)
	sheet = book.sheet_by_index(0)

	cur_group = ''
	in_group = False
	total_sum = 0

	for row_index in range(sheet.nrows):
		if (sheet.cell(row_index, 0).value == ''):
			in_group = False
			cur_group = ''
			total_sum = 0
			g = ''
		elif in_group == False:
			cur_group = sheet.cell(row_index, 0).value
			opt_value_group = int(sheet.cell(row_index,1).value)
			in_group = True
			g = FoodGroup(name=cur_group, optimal_number = opt_value_group, current_number = 0)
			g.save()
		else:
			name = sheet.cell(row_index, 0).value
			current_value = int(sheet.cell(row_index, 1).value)
			opt_value = int(sheet.cell(row_index, 2).value)
			total_sum += current_value
			i = FoodItem(name=name, foodgroup = g, optimal_number=opt_value, current_number= current_value)
			i.save()

	return 'done'