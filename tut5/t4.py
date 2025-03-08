user_connections = { "Alice": ["Bob", "Charlie", "David", "Eve", "Frank"],
                     "Bob": ["Alice", "Charlie", "Eve", "Frank"],
                     "Charlie": ["Alice", "Bob", "David"],
                     "David": ["Alice", "Charlie"],
                     "Eve" : ["Alice","Bob"],
                     "Frank" : ["Bob"]}

def hops(names, n):
  if n <= 0:
    return names

  names_ = names[:]
  for x in names:
    for y in user_connections[x]:
      if y not in names_:
        names_.append(y)
  return hops(names_, n-1)

print(set(hops(['Frank'], 1)))
print(set(hops(['Frank'], 2)))
print(set(hops(['Eve', 'Frank'], 1)))