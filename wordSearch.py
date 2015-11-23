from bsddb3 import db
import sys

def incrementLastLetter(word,amount):
	return (chr(ord(word[-1])+amount))

def search(word, partial, index):
	index = db.DB()
	index.open(index)

	curs = index.cursor()
	
	results = []

	if partial:
		#print("Doing partial.")
		if word[-1] == "%":
			word = word[:-1]
		maxWord = word[:-1] + incrementLastLetter(word,1)
		#print(maxWord)
		iter = curs.set_range(word.encode('utf-8'))
		while iter and iter[0].decode('utf-8') < maxWord:
			results.append(iter[1].decode('utf-8'))
			iter = curs.next()
	else:
		#print("Doing Full.")
		iter = curs.set(word.encode('utf-8'))
		while iter:
			results.append(iter[1])
			iter = curs.next_dup()

	return results

