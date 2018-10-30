import requests
import json
import datetime
import sys

handle = input("Enter CF Handle: ")
res = requests.get("http://codeforces.com/api/user.status?handle="+handle)
if(res.status_code<200 or res.status_code>=300):
	print("Error")
	sys.exit(0)
cur = datetime.datetime.now()
i = 0
js = res.json()
js = js['result']
print("Problems Solved Today:")
flg = 1
while flg==1 and i<len(js):
	now = datetime.datetime.fromtimestamp(js[i]['creationTimeSeconds'])
	if(cur.day == now.day and cur.month==now.month and cur.year==now.year):
		if(js[i]['verdict'] == "OK"):
			print(str(js[i]['problem']['contestId'])+""+js[i]['problem']['index'])
		i = i+1
	else:
		break