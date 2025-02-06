requirements = {
'TCX1001': [], # No prerequisites for TCX1001.
'TCX1002': ['TCX1001'], # Pass TCX1001 to take TCX1002.
'TCX1003': ['TCX1001'], # Pass TCX1001 to take TCX1003.
'G': ['TCX1002', 'TCX1003'] # To graduate, pass at least TCX1002 or TCX1003.
}

feedbacks = [('TCX1001', 3.0), ('TCX1001', 6.5), ('TCX1002',
8.0)]

def path_to_graduate(feedbacks:list, requirements:dict):
    for x in feedbacks:
       requirements[x[0]] += [x[1]]
       requirements[x[0]] += [1]
    print(requirements)

path_to_graduate(feedbacks,requirements)


