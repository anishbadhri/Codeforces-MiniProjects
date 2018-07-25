from bs4 import BeautifulSoup
import requests
import os
import sys
if len(sys.argv) != 3:
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
direc = "./"+sys.argv[1]
ext = ".in"
txt_files_in = [i for i in os.listdir(direc) if os.path.splitext(i)[1] == ".in"]
txt_files_in = [i for i in txt_files_in if i[0:len(sys.argv[1])+3] == sys.argv[1] + "Inp"]
txt_files_out = [i for i in os.listdir(direc) if os.path.splitext(i)[1] == ".out"]
txt_files_out = [i for i in txt_files_out if i[0:len(sys.argv[1])+3] == sys.argv[1] + "Out"]
ofile = open(ques+"/"+txt_files_out[0],"r")	
cnt = 1
for i in range(min(len(txt_files_in),len(txt_files_out))):
	os.system(sys.argv[2] + " < " + ques + "/" + txt_files_in[i] + " > " + ques+"/"+ques+"Test"+'.out');
	file = open(ques+"/"+ques+"Test"+'.out',"r")
	s = file.readlines()
	s = [i.replace('\n','') for i in s]
	s = [i.strip() for i in s]
	s = [i for i in s if i != '']
	ofile = open(ques+"/"+txt_files_out[i],"r")
	ofile.seek(0)
	ss = ofile.readlines()
	ss = [i.replace('\n','') for i in ss]
	ss = [i.strip() for i in ss]
	if(ss != s):
		print("Failed at Test " + str(cnt))
		print(ss)
		print(s)
		exit(0)
	cnt=cnt+1
print("Passed all Sample Test Cases")