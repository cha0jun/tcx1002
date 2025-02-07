
def edit_distance(text1, text2):
    '''
    1. find difference in text 1 and 2 (from & to)
    2. with the 2 words, create a matrix using nested list
    3. build rows and columns
    4. locate value in matrix
    '''
    ls1 = text1.split(' ')
    ls2 = text2.split(' ')
    
    deleteWord = ''
    insertWord = ''
    
    deleteWord = list(x for x in ls1 if x not in ls2)[0]
    insertWord = list(i for i in ls2 if i not in ls1)[0]
    
    distances = []
    distances.append([idx for idx in range(len(insertWord)+1)])
    for idx in range(1,len(deleteWord)+1):
        

    
    
            
    
    
    
    print(distances)
    
    
edit_distance('I can program in Python', 'can you program in Python')
        
