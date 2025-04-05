students = [ (55, "Alice"), (60, "Bob"), (67, "Charlie"), (72, "David"), (72, "George"), (85, "Eva"), (90, "Frank") ] 

def binary_search(arr:list, target:int):
    if not arr or (len(arr) ==1 and arr[0][0] != target):
        return []
    piv_pos = len(arr)//2
    piv = arr[piv_pos]
    
    # consider a reverse palindrom search after locating mid, consider that range might be lop sided, while loop might be better 
    if target == piv[0]:
        output = [piv]
        # upper exists
        if piv_pos < (len(arr) -1): 
            upper_range = arr[piv_pos+1:]
            idx = 0
            while upper_range[idx][0] == target:
                output.append(upper_range[idx])
                idx += 1
        # lower exists
        if piv_pos > 0:
            lower_range = arr[:piv_pos]
            udx = 0
            while lower_range[udx][0] == target:
                output.append(lower_range[udx])
                udx += 1
        return output
    
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
    
        
print(binary_search(students,55))

# 59, 60 ,90