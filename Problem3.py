"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

def primes(num):
  prime = num
  prime_set = []
  i = 2
  while i < prime:
    if prime%i == 0:
      prime_set.append(i)
      prime = prime/i
      i=2
    else:
      i+=1
  prime_set.append(prime)
  print prime_set[-1]
