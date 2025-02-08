
def edit_distance(text1, text2):
    ls1 = text1.split(' ')
    ls2 = text2.split(' ')
    steps = 0
    for x in ls1:
        if x not in ls2:
            steps += 1
    for i in ls2:
        if i not in ls1:
            steps += 1
    return steps
    
    
    
    
    
print(edit_distance('I can program in Python', 'can you program in Python'))
        
