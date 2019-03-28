import requests
import json
import random
import os
def getProblemURL(user_rating,problem_list):
	filtered_problem = [i for i in problem_list if i['rating']>=user_rating-50 and i['rating']<=user_rating+150]
	random_problem = random.choice(filtered_problem)
	#https://codeforces.com/problemset/problem/400/B
	return "https://codeforces.com/problemset/problem/"+str(random_problem['contestId'])+"/"+random_problem['index']
def getRandomProblem(user_handle):
	resp = requests.get("https://codeforces.com/api/user.status?handle="+ user_handle + "&from=1");
	if resp.status_code < 200 or resp.status_code>299:
		print("Error in Request")
		quit()
	all_attempted_problems = resp.json()['result']
	solved_problems = [x["problem"] for x in all_attempted_problems if x["verdict"]=="OK"]
	# print(solved_problems)
	resp = requests.get("https://codeforces.com/api/problemset.problems");
	if resp.status_code < 200 or resp.status_code>299:
		print("Error in Request")
		quit()
	all_problems = resp.json()['result']['problems']
	solved_problems = [x for x in solved_problems if 'rating' in x.keys()]
	solved_problems = [i for n, i in enumerate(solved_problems) if i not in solved_problems[n+1:]]
	unsolved_problems = [x for x in all_problems if not x in solved_problems]
	solved_problems = sorted(solved_problems,key=lambda k:k['rating'],reverse = True)
	unsolved_problems = [x for x in unsolved_problems if 'rating' in x.keys()]

	#Rating Calculation
	it = 0
	rating_average = 0
	while it<100 and it<len(solved_problems):
		rating_average += solved_problems[it]['rating']
		it = it + 1
	rating_average/=it

	cf_url = getProblemURL(rating_average,unsolved_problems)
	return cf_url