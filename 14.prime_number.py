#using flag
def prime_num(n):
  flag = False
  if n>1:
    for i in range(2, (n//2+1)):
      if n%i==0:
        flag = True
        break
  if flag:
    return "No prime"
  else:
    return "yes prime"

# print(prime_num(5))

#using for else
def prime_for_else(n):
  if n>1:
    for i in range(2, n//2+1):
      if n%i ==0:
        print("No its not prime number")
        break
    else:
      print("yes it is prime")
  else:
    print("No its not prime")

# prime_for_else(5)

# within range of number
def prime_range(start,end):
  for n in range(start,end):
    if n>1:
      for i in range(2, n//2+1):
        if n%i ==0:
          # print("No its not prime number")
          break
      else:
        # print("yes it is prime")
        print(n)
    else:
      pass
      # print("No its not prime")

prime_range(13,76)
