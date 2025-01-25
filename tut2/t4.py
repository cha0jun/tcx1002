course_credits = { "TCX1010" : 4 , "CS1234" : 2 , "TCX1101" : 4, "TCX2002" : 4 , "TCX2003" : 2 , "TCX2004" : 4}

def grades_needed(curr_gpa, target_gpa, courses): 

  # curr_gpa: (4.4, 6) 
  # target_gpa: 4.5 
  # courses: [['TCX2002', 4, None], ['TCX2003', 2, None], ['TCX2004', 4, None]] 

  def gpa(curr_gpa, courses): 
    sum = curr_gpa[0] * curr_gpa[1] 
    credits = curr_gpa[1] 
    for c in courses: 
      if c[2]: 
        sum += c[1] * c[2] 
        credits += c[1] 
    return sum/credits, credits 
 
  def course_list(lst): 
    res = [] 
    for c in lst: 
      res.append(c[0]) 
    return res 
  courses = sorted(courses, key=lambda x:x[1], reverse=True) 

  completed_courses = [x for x in courses if x[2]] 

  if len(completed_courses) >= 2 and gpa(curr_gpa, completed_courses)[0] >= target_gpa: 
          return [completed_courses] 
  best_courses = [] 
  for i in range(len(courses)): 
    c, courses_ = courses[i], courses[:i] + courses[i+1:]   
    if c[2] == None:   # choose one of the unfinished courses 
      for g in [x/2 for x in range(2, 11)]:  # for each possible grade 
        c[2] = g 
        res = grades_needed(curr_gpa, target_gpa, courses) 
        if res: 
          if len(best_courses) == 0 or sum([x[1] for x in res[0]]) < sum([x[1] for x in best_courses[0]]): 
            best_courses = [] 
            for x in res: 
              if course_list(x) not in [course_list(y) for y in best_courses]: 
                best_courses.append([y[:] for y in x]) 
          elif sum([x[1] for x in res[0]]) == sum([x[1] for x in best_courses[0]]): 
            for x in res: 
              if course_list(x) not in [course_list(y) for y in best_courses]: 
                best_courses.append([y[:] for y in x]) 
        c[2] = None 
  return best_courses 
  
def return_grade(gpa:float):
    grade = {
        5.0 :'A',
        4.5 : "A-",
        4.0 : 'B+',
        3.5: 'B',
        3.0: 'B-',
        2.5: 'C+',
        2.0: 'C',
        1.5: 'D+',
        1.0: 'D',
        0: 'F'
    }
    return grade[gpa]

# Add you code below this line
def aim_1st_class(curr_gpa:tuple, courses:list):
    ls = []
    for x in courses:
        units = course_credits[x]
        ls.append([x,units,None])
    combi = grades_needed(curr_gpa,4.5,ls)
    res = []
    for i in combi:
        res.append([(i[0][0],i[0][1],return_grade(i[0][2])),(i[1][0],i[1][1],return_grade(i[1][2]))])
    return res
    
    
    
print(aim_1st_class((4.4,6),['TCX2002', 'TCX2003', 'TCX2004']))