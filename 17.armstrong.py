def arm(n):
  t=n
  r=0
  while(t>0):
    d= t%10
    r += d**3
    t=t//10
  if (n==r):
    print("armstrong")
  else:
    print("no")

arm(153)