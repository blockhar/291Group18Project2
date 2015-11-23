import sys
import wordSearch
import searchScore
#import dateSearch
import printReviews

def process(queryList):
	if len(queryList) <= 0:
		print("Invalid query: no terms.")
		sys.exit()

	finalResults = ['Initialized']
	minDate = -1
	maxDate = -1
	minPrice = -1
	maxPrice = -1

	#print(queryList)

	while len(queryList) > 0:

		term = queryList.pop(0)	

		results = []
		
		if term == 'r:':
			word = queryList.pop(0)
			if word[-1] == '%':
				results = wordSearch.search(word,True,"rt.idx")
			else:
				results = wordSearch.search(word,False,"rt.idx")
	
		elif term == 'p:':
			word = queryList.pop(0)
			if word[-1] == '%':
				results = wordSearch.search(word,True,"pt.idx")
			else:
				results = wordSearch.search(word,False,"pt.idx")

		elif term == "rscore":
			operator = queryList.pop(0)
			if operator == '<' or operator == '>':
				pass
			else:
				print("Invalid operator: " + operator + " with term " + term)
				sys.exit()
			score = queryList.pop(0)
			try:
				score = eval(score)
			except:
				print("Invalid score: " + score)
				sys.exit()
			results = searchScore.searchScores(score, operator)

		elif term == "pprice":
			operator = queryList.pop(0)
			if operator == '<':
				price = queryList.pop(0)
				maxPrice = price
				continue
			elif operator == '>':
				price = queryList.pop(0)
				minPrice = price
				continue
			else:
				print("Invalid operator: " + operator + " with term " + term)
				sys.exit()

		elif term == "rdate":
			operator = queryList.pop(0)
			if operator == '<':
				rdate = queryList.pop(0)
				maxDate = rdate
				continue
			elif operator == '>':
				rdate = queryList.pop(0)
				minDate = rdate
				continue
			else:
				print("Invalid operator: " + operator + " with term " + term)
				sys.exit()

		else:
			if term[-1] == '%':
				results1 = wordSearch.search(term,True,"rt.idx")
				results2 = wordSearch.search(term,True,"pt.idx")
				results = set(results1) | set(results2)
			else:
				results1 = wordSearch.search(term,False,"rt.idx")
				results2 = wordSearch.search(term,False,"pt.idx")
				results = set(results1) | set(results2)

		if finalResults == ['Initialized']:
			finalResults = results
		else:
			finalResults = set(finalResults)&set(results)

	#print(list(finalResults))
	finalResults = list(finalResults)
	finalResults.sort()
	printReviews.printReviews(finalResults, maxPrice, minPrice, minDate, maxDate)


if __name__ == '__main__':
	l = ['p:', 'cam%', 'r:', 'camera', 'cam', 'rdate', '>', '19904']
	process(l)
