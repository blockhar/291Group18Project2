from bsddb3 import db
import sys

def toNum(num):
	num = num.replace("'","")
	return(eval(num))

def searchScores(score, operator):
	index = db.DB()
	index.open("sc.idx")

	curs = index.cursor()
	
	results = []

	if operator == '<':
		iter = curs.first()
		while iter and toNum(iter[0].decode('utf-8')) < score:
			results.append(iter[1].decode('utf-8'))
			iter = curs.next()

	elif operator == '>':
		iter = curs.set_range(str(score).encode('utf-8'))
		if toNum(iter[0].decode('utf-8')) == score:
			iter = curs.next_nodup()
		while iter:
			results.append(iter[1].decode('utf-8'))
			iter = curs.next()

	else:
		print("What the hell." + operator + " is not ok.")
		sys.exit()

	return results

if __name__ == '__main__':
	score = eval(input("Input score: "))
	op = input("Operator: ")

	results = searchScores(score,op)
	
	print(results)
