#Search review summ/text
from bsddb3 import db
import sys

def searchFiles(word, partial):
	index = db.DB()
	index.open("rt.idx")

	curs = index.cursor()
	iter = curs.first()

	results = []
	while iter:
		current = iter[0].decode("utf-8")
		currentID =iter[1].decode("utf-8")
		if word in current and partial==True:
 			results.append(currentID)
		elif word == current:
 			results.append(currentID)

		iter = curs.next()

	curs.close()
	index.close()
	

	return results


if __name__ == '__main__':
	partial = False
	word = input("Enter Word: ")
	partial = input("Partial Matches? (y/n)")

	if partial.upper() == 'Y':
		partial = True

	word = word.lower()
	results = searchFiles(word,partial)
	
	print(results)