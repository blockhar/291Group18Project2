import sys
from bsddb3 import db

# theData is type date and isGreater is boolean
def dateSearch(theDate, isGreater)
	index = db.DB()
	index.open("pt.idx")
	
	curs = index.cursor()
	
	results = []
	dateIndex #initialize this!
	idIndex #initialize this!
	
	while row = curs.next()
        if (row[dateIndex] > theDate and isGreater) or (row[dateIndex] < theDate and !isGreater)
            results.append(row[idIndex])
    
    
    return results
    
