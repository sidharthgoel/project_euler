

def difference(num):
  sum_of_squares = sum([x**2 for x in range(1,num+1)])
  square_of_sum = sum([x for x in range(1, num+1)])**2
  print square_of_sum - sum_of_squares
