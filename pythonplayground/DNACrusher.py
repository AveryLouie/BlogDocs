def fasta_to_string(file_object):
	string=''
	file_object.readline()
	for line in file_object:
		line=line.rstrip('\n')
		line=line.rstrip('\r')
		string+=line

	return string

def reverse(string_object):
	string=''
	string=string_object[::-1]
	return string

def complement(string_object):
	string=''
	chars=''
	CDNA={'a':'t','c':'g','t':'a','g':'c','n':'n','A':'T','C':'G','T':'A','G':'C','N':'N'}
	string=[CDNA[char] for char in string_object]
	for char in string:
		chars+=char
	return chars

def crush(seq1,seq2,length):
	count=0
	run=0
	switch=0
	record=0
	fwd=seq1[len(seq1)-length::]
	rev=seq2[:length]
	for x in range(length):
		if (fwd[x]==rev[x]):
			count+=1
			switch=1
		else:
			switch=0
			if run>record:
				record=run
			else:
				run=0 
		if switch==1:
			run+=1
	return (count,record)

def allign(seq1, seq2, expected):
	count=[]
	for x in range(expected):
		count.append((x,crush(seq1,seq2,x)))
	return count
