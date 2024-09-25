lst = [5,2,1,3,6,4]
n=len(lst)
k=9
for i in range(n):
  for j in range(i+1,n):
    if lst[i]+lst[j] == k:
      print(lst[i],lst[j])