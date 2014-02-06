prev,curr = 1, 2
total = 0
while curr < 4000000:
	if curr%2==0:
		total += curr
	prev,curr = curr, prev+curr
print(total)
	
