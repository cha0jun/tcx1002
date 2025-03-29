students = {
    "Alice":["Charlie", "David", "Eric"],
    "Bob":["Charlie", "Eric"],
    "Charlie":["Bob", "Alice", "David"],
    "David":["Bob", "Alice", "Charlie", "Eric"],
    "Eric":["Alice", "David"]
}

def find_groups(unallocated:list, current_groups:list, pref_pairs:list, original_dist:dict):
    # base case
    if not unallocated:
        return current_groups
    
    # init local vars
    new_current_groups = current_groups
    new_unallocated = unallocated
    s1 = new_unallocated[0]
    remaining_students = new_unallocated[1:]

    # case where only 3 students left
    if len(new_unallocated) == 3 :
        # try to form a group
        s2 = new_unallocated[1]
        s3 = new_unallocated[2]
        
        if s2 in original_dist[s1] and s3 in original_dist[s1] and s1 in original_dist[s2] and s3 in original_dist[s2] and s1 in original_dist[s3] and s2 in original_dist[s3]:
            sortedls = [s1,s2,s3]
            sortedls.sort()
            tup = (sortedls[0],sortedls[1],sortedls[2])
            new_current_groups.append(tup)
            return new_current_groups
        
        print("group 3 false")
        return None
        
    for s2 in remaining_students:
        if (s1,s2) in pref_pairs or (s2,s1) in pref_pairs:
            print(s1,s2)
            new_current_groups.append((s1,s2))
            new_unallocated.remove(s1)
            new_unallocated.remove(s2)
            result = find_groups(new_unallocated, new_current_groups, pref_pairs, original_dist)
            if result:
                return result
            # backtrack
            new_current_groups.remove((s1,s2))
            new_unallocated.append(s1)
            new_unallocated.append(s2)
    
    result = find_groups(new_unallocated,new_current_groups,pref_pairs,original_dist)
    if result:
        return result
    
            
    

def build_preferences(students:dict):
    if not students:
        return None
    
    stu_pairs = []
    # iterate students to check preference
    for s1 in students.keys():
        # print(s1)
        # print(students[s1])
        for pref in students[s1]:
            # check in s1 is also a prefs for s2
            if s1 in students[pref]:
                # check for duplicates in confirmed pairs for both orders
                if (s1,pref) not in stu_pairs and (pref,s1) not in stu_pairs :
                    stu_pairs.append((s1,pref))
    return stu_pairs

def allocate(students:dict):
    prefs = build_preferences(students)
    unallocated = list(students.keys())
    current_groups = []
    if len(unallocated) == 1:
        return None
    groups = find_groups(unallocated, current_groups, prefs,students)
    
    return groups

print(allocate(students))
