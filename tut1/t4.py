Sem2_results = [["Aaron", "A", "B+", "B"], ["Ben", "B", "B+", "C"], ["Carol", "A", "A", "A"], 
                ["David", "B", "B", "B"], ["Eve", "A", "A", "A-"], ["Fen", "A", "B", "C"],
                ["Gordon", "B", "C", "D"], ["Hannah", "A-", "A"], ["Ian", "A", "A"], ["John", "A","A","A-"],["Lila", "A", "B", "C"],["Steward", "A", "B", "C"]]

def return_cap(grade:str):
    cap = {
        'A+': 5.0,
        'A': 5.0,
        'A-':4.5,
        'B+':4.0,
        'B': 3.5,
        'B-': 3.0,
        'C+': 2.5,
        'C': 2.0,
        'D+': 1.5,
        'D': 1.0,
        'F': 0
    }
    return cap[grade.upper()]


def get_deans_list(Sem2_results:list):
    eligible = []
    final = []
    for x in Sem2_results:
        if len(x) > 3:
            name = x[0]
            cap = x[1:]
            gpa = 0
            idx = 0
            for i in cap:
                gpa = gpa + return_cap(i)
                idx += 1
            eligible.append((name,round((gpa/idx),2)))
    
    if len(eligible)%5 == 0:
        cutoff = int(len(eligible)/5)
    else:
        cutoff = int(len(eligible)/5) +1
    
    eligible.sort(reverse=True, key = lambda tup:tup[1])
    
    idx = 0
    curr = 0.0
    for i in eligible:
        if idx < cutoff:
            final.append(i)
            curr = i[1]
            idx += 1
        else:
            if i[1] == curr:
                final.append(i)
    return(final)

    
    
print(get_deans_list(Sem2_results))
    