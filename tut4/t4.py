user_connections = { "Alice": ["Bob", "Charlie", "David", "Eve", "Frank"],
                     "Bob": ["Alice", "Charlie", "Eve", "Frank"],
                     "Charlie": ["Alice", "Bob", "David"],
                     "David": ["Alice", "Charlie"],
                     "Eve" : ["Alice","Bob"],
                     "Frank" : ["Bob"]}
                     
def get_mutuals(main:str, sub:str, connections:dict):
    res = []
    
    main_connections = connections[main]
    sub_connections = connections[sub]
    
    for i in sub_connections:
        if i not in main_connections and i != main:
            for x in connections[i]:
                if x in main_connections:
                    res.append(i)
    return res


                

def friend_suggestion(user_connections:dict):
    res = {}
    for key in user_connections.keys():
        res[key] = []
        templist = []
        for subkey in user_connections.keys():
            if key != subkey:
                templist.extend(get_mutuals(key,subkey,user_connections))
        templist.sort()
        for rec in templist:
            if rec not in res[key]:
                res[key].append(rec)
            
    return res
    

print(friend_suggestion(user_connections))
