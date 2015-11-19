from bsddb3 import db
import sys

def searchScores(score, operator):
	index = db.DB()
	index.open("sc.idx")

	curs = index.cursor()
	
	results = []

	if operator == '<':
		iter = curs.first()
		while iter and iter[1] < score:
			results.append(iter[1])
			iter = curs.next()

	elif operator == '>':
		iter = curs.set_range(score)
		while iter:
			results.append(iter[1])
			iter = curs.next()

	else:
		print("What the hell." + operator + " is not ok.")
		sys.exit()

	return results
