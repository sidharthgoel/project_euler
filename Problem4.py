def is_palindrome(x):
	x= str(x)
	i = 0
	while i<len(x)//2:
		if x[i] == x[-1*i -1]:
			i+=1
		else:
			return False
	return True

def palindrome(x):
	return str(x) == str(x)[::-1]


