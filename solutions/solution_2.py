def next_even_number(n):
  if n % 2 == 0:
      next_even = n + 2
  else:
      next_even = n + 1
  return next_even
n=int(input("enter a number:"))
result = next_even_number(n)
print(result)
