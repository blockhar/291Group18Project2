import sys
import re
from bsddb3 import db

# information is all of the product information
def checkDate(information, reviewDate, lowDate, highDate):
    if lowDate == -1 and highDate == -1:
      return true
    
    #convert lowDate and/or highDate to correct format
    
    dateIndex = 7 # this is the minimum possible value
    
    infoArray = information.split(",")
    while not re.match(r"\D(\d{10})\D", infoArray[dateIndex]):
      dateIndex += 1
    
    if not(lowDate != -1 or lowDate < infoArray[dateIndex]) and not(highDate != -1 or highDate > infoArray[dateIndex]):
      return true
    return false

if __name__ == '__main__':
	#Might need to convert string to date here
	#checkDate(1182816000, 1)
	#checkDate(1182816000, 0)
