# This_is_a_morning
# o/p - tTHIS.is.a.mORNING
def string_mal(s='This_is_a_morning'):
  ls = []
  new_s = s.split("_")
  for i in new_s:
    ls.append(i[0].lower()+i[1:].upper())
  print(".".join(ls))

string_mal()
  
