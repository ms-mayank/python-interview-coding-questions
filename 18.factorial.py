def factorial(n):
  f = 1
  for i in range(1,n+1):
    f=f*i
  return f

# print(factorial(4))

def recursion_factorial(n):
  if n==1:
    return 1
  else:
    return n * recursion_factorial(n-1)

print(recursion_factorial(2))