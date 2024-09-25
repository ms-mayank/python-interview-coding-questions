n = 121
temp = n
rev_n = 0
while (temp>0):
  digit = temp % 10
  rev_n = rev_n*10 + digit
  temp = temp//10

if n == rev_n:
  print("yes")
else:
  print("no")