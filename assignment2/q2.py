students = [
    {"name": "Alice", "preferences": ["French", "Spanish"]},
    {"name": "Bob", "preferences": ["Spanish", "French"]},
    {"name": "Charlie", "preferences": ["French"]},
    {"name": "David", "preferences": ["French", "Spanish"]},
    {"name": "Eva", "preferences": ["French", "Spanish", "German"]},
]

classes = {
    "French": 2,  # Maximum 2 students
    "Spanish": 2,
    "German": 1,
}

def assign_students(students, classes):
    classes_ = classes.copy()

    def assign_student(remaining_students,current_assignment):
        if not remaining_students:
            return current_assignment
        
        student = remaining_students[0]
        others = remaining_students[1:]
        
        for preference in student['preferences']:
            if preference in classes_ and classes_[preference] > 0:
                classes_[preference] -= 1
                if preference not in current_assignment:
                    current_assignment[preference] = []
                current_assignment[preference].append(student['name'])

                result = assign_student(others, current_assignment)
                
                if result:
                    return result
                
                classes_[preference] += 1
                current_assignment[preference].pop()
                if not current_assignment[preference]:
                    del current_assignment[preference]
                    
    return assign_student(students,{})

result = assign_students(students,classes)
print(result)