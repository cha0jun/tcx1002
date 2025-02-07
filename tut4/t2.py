requirements = {
'TCX1001': [], # No prerequisites for TCX1001.
'TCX1002': ['TCX1001'], # Pass TCX1001 to take TCX1002.
'TCX1003': ['TCX1001'], # Pass TCX1001 to take TCX1003.
'G': ['TCX1002', 'TCX1003'] # To graduate, pass at least TCX1002 or TCX1003.
}

feedbacks = [('TCX1001', 3.0), ('TCX1001', 6.5), ('TCX1002',
8.0)]

def get_avg(feedbacks:list):
    res = {}
    for x in feedbacks:
        if x[0] not in res:
            res.update({x[0]:x[1]})
        else:
            val = res[x[0]]
            res.update({x[0]:(val+x[1])/2})
    return res

def build_path(mod:str,requirements:dict):
    res = []
    isBuilt = False
    currMod = mod
    while isBuilt == False:
        res.append(currMod)
        ls = requirements[currMod]

    return res
            


def path_to_graduate(feedbacks:list, requirements:dict):

    avg_scores = get_avg(feedbacks)
    
    to_grad = requirements['G']
    
    print(to_grad)
    
##path_to_graduate(feedbacks,requirements)

print(build_path('TCX1003',requirements))