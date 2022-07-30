def array_diff(a, b):
  c= [item for item in a if item not in b]
  return c

print(array_diff([1,2],[1]))