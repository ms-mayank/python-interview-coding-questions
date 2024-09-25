def sc_high(l):
  if l[0]>l[1]:
    f = l[0]
    s = l[1]
  else:
    f = l[1]
    s=l[0]
  for i in range(2,len(l)):
    if l[i]>f:
      s=f
      f=l[i]
    elif l[i]>s and f!=l[i]:
      s=l[i]
  return s

print(sc_high([1,4,2,6,2,7,2,7,7]))

def second_largest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort(reverse=True)
    
    return unique_numbers[1] if len(unique_numbers) >= 2 else None

numbers = [10, 20, 4, 45, 99, 99, 45]

result = second_largest(numbers)

if result:
    print("The second largest number is:", result)
else:
    print("The list does not have enough unique elements.")