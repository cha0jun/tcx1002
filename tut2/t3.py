Student_Sem2_Results = [{"studentID":"ID1234A", "Course":"TCX1010", "Grade":"A"},
{"studentID":"ID1234A", "Course":"CS1234", "Grade":"B+"},
{"studentID":"ID1234A", "Course":"TCX1101", "Grade":"A"},
{"studentID":"ID2345B", "Course":"TCX1010", "Grade":"B"},
{"studentID":"ID2345B", "Course":"CS1234", "Grade":"B-"},
{"studentID":"ID3456C", "Course":"TCX1010", "Grade":"B+"},
{"studentID":"ID3456C", "Course":"CS1234", "Grade":"B"},
{"studentID":"ID3456C", "Course":"TCX1101", "Grade":"C+"}]

course_credits = { "TCX1010" : 4 , "CS1234" : 2 , "TCX1101" : 4, "TCX2002" : 4 ,
"TCX2003" : 2 , "TCX2004" : 4}

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

def curr_sem_gpa(Student_Sem2:list):
    output = {}
    for x in Student_Sem2:
        id = x['studentID']
        if id not in output.keys():
            output[id] = (0,0)
        units = course_credits[x['Course']]
        cap = return_cap(x['Grade'])
        credits = output[id][1]
        gpa = ((cap*units) + (output[id][0] *credits))/(credits+units)
        output.update({id:(round(gpa,2),credits+units)})
    return output
print(curr_sem_gpa(Student_Sem2_Results))
            