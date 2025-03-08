students = [
    ('Alice', 'F', 1),
    ('Bob', 'M', 2),
    ('Charlie', 'M', 3),
    ('Diana', 'F', 4)
]

def committee_selection(students):
  def all_subset(lst):
    if len(lst) == 0:
      return [[]]
    head, temp = lst[0], all_subset(lst[1:])
    return temp + [[head] + x for x in temp]

  res = []
  for s in all_subset(students):
    m = sum([1 for x in s if x[1] == 'M'])
    f = sum([1 for x in s if x[1] == 'F'])
    y12 = sum([1 for x in s if x[2] <= 2])
    y34 = sum([1 for x in s if x[2] >= 3])
    if -1 <= m-f <= 1 and y12>=1 and y34>=1:
      res.append(s)
  return sorted(res)

for row in committee_selection(students):
  print(row)

print()

for row in committee_selection(students[:3]):
  print(row)
            
            


