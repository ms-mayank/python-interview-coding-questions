s="iitinnnsnfsiieieslstsd"
sd = {}
for i in s:
  if i in sd:
    sd[i]= sd[i]+1
  else:
    sd[i]= 1

print(sd['f'])