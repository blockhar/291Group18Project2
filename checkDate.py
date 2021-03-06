import sys
import re
import time
import datetime

# information is all of the product information
def checkDate(information, lowDate, highDate):
    if lowDate == -1 and highDate == -1:
      return True
    
    #convert lowDate and/or highDate to correct format
    if not lowDate == -1:
    	lowDate = int(time.mktime(datetime.datetime.strptime(lowDate, '%Y/%m/%d').timetuple()))  #time.strptime(lowDate, '%Y/%m/%d')
    if not highDate == -1:
    	highDate = int(time.mktime(datetime.datetime.strptime(highDate, '%Y/%m/%d').timetuple()))  #time.strptime(highDate, '%Y/%m/%d')
    
    dateIndex = 7 # this is the minimum possible value
    
    infoArray = information.split(",")
    #print(infoArray)
    while not re.match('[0-9]{9}', infoArray[dateIndex]):
      dateIndex += 1
    
    result = True
    if(lowDate != -1):
    	if not lowDate < int(infoArray[dateIndex]):
    		result = False
    if(highDate != -1):
    	if not highDate > int(infoArray[dateIndex]):
    		result = False
    return result

if __name__ == '__main__':
	print( checkDate("B000GKXY34,Nun Chuck,Novelty Nun Toss Toy,17.99,ADX8VLDUOL7BG,M. Gingras,0/0,5.0,1262304000,Great fun!,Got these last Christmas as a gag gift. They are great fun, but obviously this is not a toy that lasts!",'1994/01/01','1995/01/01'))
	print( checkDate("B000GKXY34,Nun Chuck,Novelty Nun Toss Toy,17.99,ADX8VLDUOL7BG,M. Gingras,0/0,5.0,1262304000,Great fun!,Got these last Christmas as a gag gift. They are great fun, but obviously this is not a toy that lasts!",'1994/01/01','2015/10/10'))
	print( checkDate("B000GKXY34,Nun Chuck,Novelty Nun Toss Toy,17.99,ADX8VLDUOL7BG,M. Gingras,0/0,5.0,1262304000,Great fun!,Got these last Christmas as a gag gift. They are great fun, but obviously this is not a toy that lasts!",-1,'2015/10/10'))
	print( checkDate("B000GKXY34,Nun Chuck,Novelty Nun Toss Toy,17.99,ADX8VLDUOL7BG,M. Gingras,0/0,5.0,1262304000,Great fun!,Got these last Christmas as a gag gift. They are great fun, but obviously this is not a toy that lasts!",'1994/01/01',-1))
	print( checkDate("B000GKXY34,Nun Chuck,Novelty Nun Toss Toy,17.99,ADX8VLDUOL7BG,M. Gingras,0/0,5.0,1262304000,Great fun!,Got these last Christmas as a gag gift. They are great fun, but obviously this is not a toy that lasts!",-1,-1))
