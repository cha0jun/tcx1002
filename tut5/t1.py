def return_cap(grade):
  if grade == 'A+' or grade == 'A':
    return 5.0
  elif grade == 'A-':
    return 4.5
  elif grade == 'B+':
    return 4.0
  elif grade == 'B':
    return 3.5
  elif grade == 'B-':
    return 3.0
  elif grade == 'C+':
    return 2.5
  elif grade == 'C':
    return 2.0
  elif grade == 'D+':
    return 1.5
  elif grade == 'D':
    return 1.0
  else:
    return 0.0

input=[('TCX1001', 4, 'A-'), ('TCX1002', 4, 'B+'),
('TCX1003', 2, 'A')]
    
def calc_gpa(input:list):
  ##base case, all items in list have been iterated
  if not input:
    return (0,0)
  else:
    gpa,credits = calc_gpa(input[1:])
    sum = gpa * credits + return_cap(input[0][2])*input[0][1]
    credits += input[0][1]
    return (round(sum/credits,1),credits)
  
print(calc_gpa(input))
      
    
    


    
        
    