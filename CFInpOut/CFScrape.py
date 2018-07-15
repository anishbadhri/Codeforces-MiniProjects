from bs4 import BeautifulSoup
import requests
import os
import sys
if len(sys.argv) != 2:
	print("Please Refer README.md for Syntax")
	exit(1)
ques = sys.argv[1]
num = ques[:len(ques)-1]
dif = ques[len(ques)-1]
page_link = 'http://codeforces.com/contest/'+num+'/problem/'+dif
print(page_link)
page_response = requests.get(page_link, timeout=10)
page_content = BeautifulSoup(page_response.content, "html.parser")
if len(page_content.find_all("div",attrs={"class":"input"})) > 0:
	if(os.path.exists("./"+ques)==False):
		os.mkdir("./"+ques)
for i in range(0, len(page_content.find_all("div",attrs={"class":"input"}))):
	paragraphs = page_content.find_all("div",attrs={"class":"input"})[i].pre.get_text(strip=True,separator="\n")
	file = open(ques+"/"+ques+"Inp"+str(i+1)+'.in',"w+")
	file.write(paragraphs)
for i in range(0, len(page_content.find_all("div",attrs={"class":"output"}))):
	paragraphs = page_content.find_all("div",attrs={"class":"output"})[i].pre.get_text(strip=True,separator="\n")
	file = open(ques+"/"+ques+"Out"+str(i+1)+'.out',"w+")
	file.write(paragraphs)