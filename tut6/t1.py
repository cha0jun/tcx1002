def edit_distance(text1:str, text2:str):

    if not text1 and not text2: ##base
        steps = 0
        return steps
    
    if not text1: ##text1 empty
        steps = len(text2) - len(text1)
        return steps
    elif not text2:
        steps = len(text1) - len(text2)
        return steps
    
    if (text1[0] not in text2) or (text2[0] not in text1):
        steps = 1
        return steps + edit_distance(text1[1:],text2[1:])
    
    
    return edit_distance(text1[1:],text2[1:])
    
    
print(edit_distance('cat','walk'))
    

        