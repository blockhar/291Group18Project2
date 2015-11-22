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
		print("Doing partial.")
		if word[-1] == "%":
			word = word[:-1]
		maxWord = word[:-1] + incrementLastLetter(word,1)
		iter = curs.set_range(word.encode('utf-8'))
		while iter and iter[1].decode('utf-8') < maxWord:
			results.append(iter[1].decode('utf-8'))
			iter = curs.next()
	else:
		print("Doing Full.")
		#print(word)
		#print(word.encode('utf-8'))
		iter = curs.set(word.encode('utf-8'))
		while iter:
			results.append(iter[1])
			iter = curs.next_dup()

	return results


if __name__ == '__main__':
	word = input("Word: ")
	partial = eval(input("Partial: "))

	results = searchTitles(word, partial)

	print(results)
