from bsddb3 import db
import sys

def incrementLastLetter(word,amount):
	return (chr(ord(word[-1])+amount))

def searchTitles(word, partial):
	index = db.DB()
	index.open("pt.idx")

	curs = index.cursor()
	
	results = []

	if partial:
		if word[-1] == "%":
			word = word[:-1]
		maxWord = word[:-1] + incrementLastLetter(word,1)
		iter = curs.set_range(word)
		while iter and iter[1] < maxWord:
			results.append(iter[1])
			iter = curs.next()
	else:
		iter = curs.get(word)
		while iter:
			results.append(iter[1])
			iter = curs.next_dup()

	return results
