from bsddb3 import db
import sys
import math

# if you don't want to check pricemax or pricemin pass -1
def printReviews(results,pricemax = -1, pricemin = -1):
	index = db.DB()
	index.open("rw.idx")

	curs = index.cursor()
	iter = curs.first()

	while iter: 
		priceFlag = False
		currentID =iter[0].decode("utf-8")
		curPrice = 0
		if int(currentID) in results:

			everything = iter[1].decode("utf-8").split(",")
			flag = 0
			for i in everything:
				quoteCount = i.count("\"")
				if flag == 2 and priceFlag == False:
					#print (i)
					if i == 'unknown':
						i = -1

					if pricemin == -1 and pricemax == -1: 
					
						print (iter[1].decode("utf-8"))
						print("")

					else:
		
						inRange = checkPriceRange(pricemax, pricemin, i)
						#print(inRange)
						if inRange == True: 
							print (iter[1].decode("utf-8"))
							print("")


					flag = 0
					priceFlag = True
					break

				if '\"' in i: 
					if quoteCount == 2: 
						flag = 2
					elif flag == 0: 
						flag += 1
					else: 
						flag += 1
				
		iter = curs.next()

def checkPriceRange(priceMax, priceMin, current):

	if current == -1: 
		return False
	if priceMax == -1: 
		if float(current) >priceMin: 
			return True
	elif float(current)>priceMin and float(current)< priceMax:
		return True 

	return False

if __name__ == '__main__':
	results = [1,2,3,4,5,6,7,8,9,10]
	printReviews(results)