#  String manipulation. "The Sky is Blue" to "Blue is The Sky"

s = "The Sky is Blue"
# print(" ".join(reversed(s.split(" "))))

st = "@#sf #sdf ds %343 SDF"
res = ""
for i in st:
  if(i.isalpha() or i ==" "):
    res = res+i
print(res)