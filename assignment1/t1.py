import re

assignment_scores = [
('A1234567B_A3721123c_JohnDoe.py', 15.0),
('A2382828W-A0023458k_a2344564k.py', 6.5)
]

def validateStudentId(studentId:str):
    if studentId[0].upper() != 'A':
        return False
    if (studentId[-1]).isdigit() == True:
        return False
    digits = studentId[1:-1]
    if len(digits) != 7:
        return False
    if digits[::].isdigit() == False:
        return False
    return True


def student_scores(assignment_scores:list):
    res = {
       ## studentId: (filename, score)        
    }
    
    ##+((?!\_)+(?<!_))
    pattern = '(?<=a|A)+([\w]{8})'
    
    for x in assignment_scores:
        results = re.findall(pattern, x[0])
        for ids in results:
            ids = 'A'+ ids
            if validateStudentId(ids) == True:
                res[ids.upper()] = (x[0],x[1])
    
    return res
        

print(student_scores(assignment_scores))

    

    