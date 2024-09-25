my_dict = {'b': 3, 'a': 1, 'c': 2}
# sort by keys
print(dict(sorted(my_dict.items())))
sort_keys = {key:my_dict[key] for key in sorted(my_dict)}
# sort by values
print(dict(sorted(my_dict.items(), key = lambda item:item[1])))
sort_value = {key:value for key,value in sorted(my_dict.items(),key = lambda item:item[1])}