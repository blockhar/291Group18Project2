import fileinput

review_index = 1

def ReplaceChar(line): 
	if "\"" in line: 
		line = line.replace ('\"', '&quot;')
	if "\\" in line: 
		line = line.replace('\\','\\\\')
	return line
	

def parsefile(line,review_line,review_file,pterm_file,rterm_file,score_file):
	global review_index 

	if 'product/productId' in line: 
		line = line.replace('product/productId: ','')
		review_line = str(review_index) + "," + line 

	elif 'product/title' in line: 
		line = line.replace('product/title: ','')
		review_line += " \"" +line+ "\","
		Terms(line,pterm_file)

	elif 'product/price' in line: 
		line = line.replace('product/price: ','')
		review_line += line + ","
		
	elif 'review/userId' in line: 
		line = line.replace('review/userId: ','')
		review_line += line + ","
	
	elif 'review/profileName' in line: 
		line = line.replace('review/profileName: ','')
		review_line += " \"" +line+ "\","

	elif 'helpfulness' in line: 
		line = line.replace('review/helpfulness: ','')
		review_line += line+ ","

	elif 'review/score' in line: 
		line = line.replace('review/score: ','')
		review_line += line + ","
		Scores(line,score_file)

	elif 'review/time' in line: 
		line = line.replace('review/time: ','')
		review_line += line+ ","

	elif 'review/summary' in line: 
		line = line.replace('review/summary: ','')
		review_line += " \"" +line+ "\","
		Terms(line,rterm_file)

	elif 'review/text' in line: 
		line = line.replace('review/text: ','')
		review_line += " \"" +line+ "\""
		ReviewPrint(review_line, review_file)
		Terms(line,rterm_file)
		review_index += 1 



	return review_line

def ReviewPrint(review_line,f):
	review_line = review_line.replace('\n','')
	review_line += '\n'
	f.write(review_line)

def Terms(line,f):
	global review_index 
	words = []
	curstr = ""
	current = 0
	last = 0 

	for character in line: 
		if character.isalnum(): 
			curstr += character
		elif character == "_":
			curstr += character
		else: 
			if len(curstr)>=3:
				curstr = curstr.lower()
				f.write(curstr +","+str(review_index)+'\n')
			curstr = ""

def Scores(score,f): 
	global review_index 
	score = score.replace('\n','')
	f.write(score + "," + str(review_index) +'\n')

if __name__=="__main__": 
	review_line = ""
	review_file = open('review.txt','w')
	pterm_file  = open('pterms.txt','w')
	rterm_file  = open('rterms.txt','w')
	score_file  = open('scores.txt', 'w')

	for line in fileinput.input(): 
		line = ReplaceChar(line)
		review_line = parsefile(line,review_line,review_file,pterm_file,rterm_file,score_file)
	

	review_file.close()
	pterm_file.close()
	rterm_file.close()
	score_file.close()

