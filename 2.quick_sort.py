def quick_sort(arr):
  if len(arr)<=1:
    return arr
  else:
    pivot = arr[len(arr)//2]
    left= [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(right) + middle + quick_sort(left)

arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = quick_sort(arr)
print(sorted_arr)