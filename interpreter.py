import re
import sys
import fileinput

def readQuery(queryStr):
    #print (queryStr)
    queryParts = splitQuery(queryStr)
    toProcess = []

    '''while len(queryParts) > 0:
        term = queryParts[0]
        if term == ""
'''
    return (queryParts)

def splitQuery(queryStr):
    allTerms = queryStr.split(" ")
    lcase = []

    #remove blanks and make all lowercase
    for word in allTerms:
        if word != "":
            lcase.append(word.lower())

    tempName = []

    #handle no spaces
    for term in lcase:
        if re.match('^r:', term):
            splitTerm = term.split(":", 1)
            tempName.append("r:")
            tempName.append(splitTerm[1])

        elif re.match('^p:', term):
            splitTerm = term.split(":", 1)
            tempName.append("p:")
            tempName.append(splitTerm[1])

        elif re.match('^rscore<', term):
            splitTerm = term.split("<", 1)
            tempName.append("rscore")
            tempName.append("<")
            tempName.append(splitTerm[1])

        elif re.match('^rscore>', term):
            splitTerm = term.split(">", 1)
            tempName.append("rscore")
            tempName.append(">")
            tempName.append(splitTerm[1])

        elif re.match('^pprice<', term):
            splitTerm = term.split("<", 1)
            tempName.append("pprice")
            tempName.append("<")
            tempName.append(splitTerm[1])

        elif re.match('^pprice>', term):
            splitTerm = term.split(">", 1)
            tempName.append("pprice")
            tempName.append(">")
            tempName.append(splitTerm[1])

        elif re.match('^rdate<', term):
            splitTerm = term.split("<", 1)
            tempName.append("rdate")
            tempName.append("<")
            tempName.append(splitTerm[1])

        elif re.match('^rdate>', term):
            splitTerm = term.split(">", 1)
            tempName.append("rdate")
            tempName.append(">")
            tempName.append(splitTerm[1])

        elif re.match('^>.+', term):
            tempName.append(">")
            tempName.append(term[1:])

        elif re.match('^<.+', term):
            tempName.append("<")
            tempName.append(term[1:])

        else:
            tempName.append(term)

    finalList = []

    #remove blanks again
    for word in tempName:
        if word != "":
            finalList.append(word)
    return finalList


def process(queryList):
	
	if len(queryList) <= 0:
		print ("Invalid query: no terms.")
		sys.exit()

	results = []

	term = queryList.pop(0)
	
	if term == 'r:':
		word = queryList.pop(0)
		if re.match('\%', word):
			print("reviewSearch(" + word + ", partial)")

		else:
			print("reviewSearch(" + word + ")")

	elif re.match('^p:', term):
        splitTerm = term.split(":", 1)
        tempName.append("p:")
        tempName.append(splitTerm[1])

    elif re.match('^rscore<', term):
        splitTerm = term.split("<", 1)
        tempName.append("rscore")
        tempName.append("<")
        tempName.append(splitTerm[1])

    elif re.match('^rscore>', term):
        splitTerm = term.split(">", 1)
        tempName.append("rscore")
        tempName.append(">")
        tempName.append(splitTerm[1])

    elif re.match('^pprice<', term):
        splitTerm = term.split("<", 1)
        tempName.append("pprice")
        tempName.append("<")
        tempName.append(splitTerm[1])

    elif re.match('^pprice>', term):
        splitTerm = term.split(">", 1)
        tempName.append("pprice")
        tempName.append(">")
        tempName.append(splitTerm[1])

    elif re.match('^rdate<', term):
        tempName.append("rdate")

    elif re.match('^rdate>', term):
        tempName.append("rdate")

    elif re.match('^>.+', term):
        tempName.append(">")

    elif re.match('^<.+', term):
        tempName.append("<")	
	
	return()



if __name__ == '__main__':
    for line in fileinput.input():
    	queryList = readQuery(line.strip())
	process(queryList)






