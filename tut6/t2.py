def merge(lst1, lst2):
  idx1, idx2, res = 0, 0, []
  while idx1<len(lst1) or idx2<len(lst2):
    if idx1 < len(lst1) and idx2 == len(lst2):
      res.append(lst1[idx1])
      idx1 += 1
    elif idx1 == len(lst1) and idx2 < len(lst2):
      res.append(lst2[idx2])
      idx2 += 1
    elif lst1[idx1] <= lst2[idx2]:
      res.append(lst1[idx1])
      idx1 += 1
    else:
      res.append(lst2[idx2])
      idx2 += 1
  return res

input = [(78.5, 'A123456B'), (66, 'A234567M'), (85.5, 'A283943G')]

def merge_sort(lst:list):
    print(lst)
    if len(lst) <=1: ##base
            return lst
    ## break into 2 list
    pivot = len(lst)//2
  ## if len(lst)>2, call again
    return merge(merge_sort(lst[:pivot]), merge_sort(lst[pivot:]))
  
print(merge_sort(input))
  
  
  