s='nitin'

# if s == s[::-1]:
#   print("pallndorme")
# else:
#   print("not")


n=0
for i in range(len(s)):
  if s[i]!=s[len(s)-i-1]:
    n=1
    break
if n == 0:
  print("pallndorme")
else:
  print("not")