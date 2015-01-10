"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

def factorize(n):
	l = []
	while n > 1:
		i = 2
		while i <= n:
			if n%i == 0:
				n = n/i
				l.append(i)
			else:
				i+=1
	return l[-1]

#could be improved - we only need the last element, this however gets a list of all of them