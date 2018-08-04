import requests
import json
import sys

print("Number of Handles: ",end="")
h = int(input())
if h<=0:
	sys.exit(0)
hnd = []
print("Enter Handles: ")
while h>0:
	h = h - 1;
	s = input()
	hnd.append(s)
handleString = "handles="
for i in hnd:
	handleString += i+";"
handleString = handleString[:len(handleString)-1]
apiString = "http://codeforces.com/api/contest.standings?showUnofficial=true&"+handleString+"&contestId="
response = requests.get("http://codeforces.com/api/contest.list");
if(response.status_code < 200 or response.status_code >=300):
	sys.exit(0)
tt = response.json()
tt = tt['result']
contestList = []
print("\n")
for i in tt:
	if(i['phase'] != 'FINISHED'):
		continue
	response = requests.get(apiString + str(i['id']))
	tnew = response.json()
	tnew = tnew['result']
	if(len(tnew['rows'])==0):
		contestList.append(i['name'] + " --- " + str(i['id']))
		if(len(contestList)==5):
			for c in contestList:
				print(c)
			print("\nDisplay More[y/n]: ",end="")
			ch = input()
			if(ch!='Y' and ch!='y'):
				sys.exit(0)
			contestList = []
			print("Continuing List\n")
for c in contestList:
	print(c)