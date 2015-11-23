import sys
from bsddb3 import db

# theData is type date and isGreater is boolean
def dateSearch(theDate, isGreater):
    index = db.DB()
    index.open("rw.idx") #first column: index, second column: everything else
    
    curs = index.cursor()
    
    results = []
    dateIndex = 7
    idIndex = 0
    
    while row = curs.next():
        rowArray = row[1].split(",")
        if (rowArray[dateIndex] > theDate and isGreater) or (rowArray[dateIndex] < theDate and !isGreater):
            results.append(rowArray[idIndex])
    
    curs.close()
    index.close()
    return results
    

if __name__ == '__main__':
	#Might need to convert string to date here
	dateSearch(1182816000, 1)
	dateSearch(1182816000, 0)
