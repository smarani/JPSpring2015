from foodpantry.models import *

def reverseTable():
	sets = []
	sets2 = []
	date = DateUploaded.objects.all()[DateUploaded.objects.count()-1]
	g = date.foodgroup_set.all()
	for thing in g:
		sets.append([thing.name, thing.current_number, thing.optimal_number, thing.change, thing.deficit, thing.priority])
		h = thing.fooditem_set.all()
		for thing2 in h:
			sets.append([thing2.name, thing2.current_number, thing2.optimal_number, thing2.change, thing2.deficit, thing2.priority])
		sets2.append(sets)
		sets = []

	return sets2