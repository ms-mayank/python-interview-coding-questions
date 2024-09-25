# Normal fibonacci
def fibo(n):
  a,b = 0,1
  for _ in range(n):
    print(a)
    a,b = b,a+b
# fibo(7)

# recursion fibonacci
def rec_fibo(n):
  if n==0:
    return 0
  elif n==1:
    return 1
  else:
    return rec_fibo(n-1) + rec_fibo(n-2)

n = 9
for i in range(n):
  print(rec_fibo(i))