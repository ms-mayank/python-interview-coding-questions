def fizzbuzz(n):
  for i in range(1,n+1):
    if i%3==0 and i%5 ==0:
      print("fizzbuzz")
    elif i%3 ==0:
      print('fizz')
    elif i%5 ==0:
      print("buzz")
    else:
      print(i)
# fizzbuzz(30)

def fizzbuzz2(n):
  d = {3: 'fizz',5:'buzz'}
  for i in range(1,n+1):
    r=""
    for k,v in d.items():
      if i%k==0:
        r=r+v
    if not r:
      r = i
    print(r)
fizzbuzz2(15)