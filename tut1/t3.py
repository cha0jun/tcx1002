import csv

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
        
def return_latestCAP(student:list):
    print(student)
    with open('latestCAP.csv') as file:
        for line in file:
            i = line.split(',')
            if student[0] == i[0].replace('"',''):
                gpa = float(i[1])
                credits = int(i[2])
                grades = student[1:]
                for mod in grades:
                    gpa = ((gpa * credits) + (return_cap(mod[0]) * int(mod[1])))/ (credits + int(mod[1]))
                    credits = credits + int(mod[1])
                return (round(gpa,2),credits) 

studentA_sem2_results = ['ID1234A', ("A", 4), ("B", 4)]
studentB_sem2_results = ['ID2345B', ("A", 4), ("B+", 4), ("C", 4)]
studentC_sem2_results = ['ID3456C', ("A", 4), ("B", 4), ("A-", 4)]

print(return_latestCAP(studentA_sem2_results))
print(return_latestCAP(studentA_sem2_results))




                    
                    
                
    
    
    