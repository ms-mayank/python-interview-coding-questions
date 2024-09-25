ls = [1,24,5,2,64,6,3,8,43,34]
max_num,min_num = ls[0],ls[0]
for i in ls:
  if i>max_num:
    max_num=i
  if i<min_num:
    min_num = i
print(max_num,min_num)