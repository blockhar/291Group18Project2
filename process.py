import sys

def process(queryList):
	if len(queryList) <= 0:
		print("Invalid query: no terms.")
		sys.exit()

	results = ['Initialized']

	while len(queryList) > 0:

		term = queryList.pop(0)	
		
		if term == 'r:':
			word = queryList.pop(0)
			if word[-1] == '%':
				print("reviewSearch(" + word + ", partial)")
			else:
				print("reviewSearch(" + word + ")")
	
		elif term == 'p:':
			word = queryList.pop(0)
			if word[-1] == '%':
				print("productSearch(" + word + ", partial)")
			else:
				print("productSearch(" + word + ")")

		elif term == "rscore":
			operator = queryList.pop(0)
			if operator == '<' or operator == '>':
				pass
			else:
				print("Invalid operator: " + operator + " with term " + term)
				sys.exit()
			score = queryList.pop(0)
			print("rrscoreSearch(" + operator + " " + score + ")")

		elif term == "pprice":
			operator = queryList.pop(0)
			if operator == '<' or operator == '>':
				pass
			else:
				print("Invalid operator: " + operator + " with term " + term)
				sys.exit()
			price = queryList.pop(0)
			print("ppriceSearch(" + operator + " " + price + ")")

		elif term == "rdate":
			operator = queryList.pop(0)
			if operator == '<' or operator == '>':
				pass
			else:
				print("Invalid operator: " + operator + " with term " + term)
				sys.exit()
			rdate = queryList.pop(0)
			print("rdateSearch(" + operator + " " + rdate + ")")

		else:
			if term[-1] == '%':
				print("generalSearch(" + term + ", partial)")
			else:
				print("generalSearch(" + term + ")")




if __name__ == '__main__':
	l = ['p:', 'cam%', 'r:', 'camera', 'cam', 'rdate', '>', '19904']
	process(l)
