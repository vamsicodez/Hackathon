

def calcuate():
	""" Calcuating no of substrings of  given weight
	weight of a - 1
	     .
	     .
	     .
	weight of z - 1
	Input:
		2 - test cases
		5 - weight
		abcdef - given string
		4 = weight
		abcdef - given string 
	Output:
		2 - (bc,f)	
		1 - (b)
	"""     
	
	t_case = int(raw_input())
	while t_case!=0:
		n = int(raw_input())
		s = raw_input()
		st=0
		en=0
		tot = ord(s[0])
		tot = tot-96
		count = 0
		while True:
			if tot == n:
				
				st = st+1
				en = en+1
				count = count+1
				if en>=len(s):
					print st,en,"1"
					break
				tot = tot-(ord(s[st-1])-96)+(ord(s[en])-96)
				
				
			elif tot<n:
				en = en+1
				if en>=len(s):
					break
				tot = tot+(ord(s[en])-96)
				
			else:
				
				if st>=len(s):
					break
				tot = tot-(ord(s[st])-96)
				if st==en:
					tot = tot+(ord(s[st])-96)
					st = st+1
					en = en+1
				else:	
					st = st+1
					
		print count	
		t_case = t_case-1

if __name__="__main__":
	calculate()
