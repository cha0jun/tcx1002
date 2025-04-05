my_list = [('TCX1001', 3, 1, 4, 5, 2), ('TCX1002', 5, 8, 7, 9), ('TCX1003', 2, 5, 3, 1, 1, 1)]

def bubble_sort(lst:list):
    isSwapped = False
    for idx in range(len(lst)-1):
        first_avg = sum(lst[idx][1:])/len(lst[idx][1:])
        sec_avg = sum(lst[idx+1][1:])/len(lst[idx+1][1:])
        if first_avg > sec_avg:
            lst[idx],lst[idx+1] = lst[idx +1], lst[idx]
            isSwapped = True
    if isSwapped:
        bubble_sort(lst)
    
    return lst
        
        
print(bubble_sort(my_list))