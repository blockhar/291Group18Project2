from bsddb3 import db
import sys
import math
import checkDate

# if you don't want to check pricemax or pricemin pass -1
def printReviews(results,pricemax = -1, pricemin = -1, minDate = -1, maxDate = -1):
	index = db.DB()
	index.open("rw.idx")

	try:
		pricemin = pricemin.replace("'","")
		pricemin = float(eval(pricemin))
	except:
		pass
	try:
		pricemax = pricemax.replace("'","")
		pricemax = float(eval(pricemax))
	except:
		pass

	curs = index.cursor()
	#iter = curs.first()

	for elem in results:
		iter = curs.set(elem.encode('utf-8')) 
		priceFlag = False
		currentID =iter[0].decode("utf-8")
		curPrice = 0
		#if int(currentID) in results:
		if True:

			everything = iter[1].decode("utf-8").split(",")
			flag = 0
			for i in everything:
				quoteCount = i.count("\"")
				if flag == 2 and priceFlag == False:
					#print (i)
					if i == 'unknown':
						i = -1

					if pricemin == -1 and pricemax == -1:
						if checkDate.checkDate(iter[1].decode('utf-8'), minDate, maxDate):
							print("Entry Number: " + iter[0].decode("utf-8"))
							printPretty(iter)
							#print (iter[1].decode("utf-8"))
							#print("")

					else:
		
						inRange = checkPriceRange(pricemax, pricemin, i)
						#print(i)
						#print(inRange)
						dateOK = checkDate.checkDate(iter[1].decode('utf-8'), minDate, maxDate)
						if inRange == True and dateOK: 
							print("Entry Number: " + iter[0].decode("utf-8"))
							printPretty(iter)


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

def printPretty(iter): 
	current = 0
	everything = iter[1].decode("utf-8").split(",")

	print("Product ID: "+ everything[current])
	current+=1 

	quoteCount = everything[current].count("\"")

	if quoteCount == 1: 
		print("Title: " + everything[current]+ ","+ everything[current+1])
		current+=2
	else: 
		print("Title: " + everything[current])
		current +=1

	print("Price: " + everything[current])
	current += 1

	print ("User ID: " + everything[current])
	current += 1 

	print("Profile Name: " + everything[current])
	current +=1

	print("Helpfulness: " + everything[current])
	current += 1

	print("Score: " + everything[current])
	current += 1

	print("Time: " + everything[current])
	current += 1

	print("Summary: " + everything[current])

	print("Review: ", end="")
	for index, word in enumerate(everything):
		#print(everything[index])
		if(index>current):
			print(everything[index], end = ",")

	print("\n")


if __name__ == '__main__':
	results = ['1','2','3','4','5','6','7','8','9','10']
	printReviews(results,20,10)
