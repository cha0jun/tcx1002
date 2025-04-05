students = [ (55, "Alice"), (60, "Bob"), (67, "Charlie"), (72, "David"), (72, "George"), (85, "Eva"), (90, "Frank") ] 

def binary_search(arr:list, target:int):
    if not arr:
        return []
    piv_pos = len(arr)//2
    piv = arr[piv_pos]
    
    # consider a reverse palindrom search after locating mid, consider that range might be lop sided, while loop might be better 
    if target == piv[0]:
        return [piv]
    elif target > piv[0]:
        # target in upper half
        new_arr = arr[piv_pos:]
        result = binary_search(new_arr,target)
        return result
    elif target < piv[0]:
        # target in lower half
        new_arr = arr[:piv_pos]
        result = binary_search(new_arr,target)
        return result
    
        
print(binary_search(students,72))