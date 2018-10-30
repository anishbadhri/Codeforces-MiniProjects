import datetime

now = datetime.datetime.now()
cur = datetime.datetime.fromtimestamp(1540466922)
if(cur.day == now.day and cur.month==now.month and cur.year==now.year):
	print("Hello")