from argparse import ArgumentParser
import cf_recommend
def getInput():
	#Define Input Here
	parser = ArgumentParser()
	parser.add_argument("-cf","--codeforces",required=True )
	args = parser.parse_args()
	user_handles = {
		"codeforces" : args.codeforces
		}
	return user_handles

def main():
	parameter = getInput()
	open_url = []
	if parameter["codeforces"] != None:
		open_url.append(cf_recommend.getRandomProblem(parameter["codeforces"]))

if __name__ == "__main__":
	main()