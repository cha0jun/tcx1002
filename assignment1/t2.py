def min_workers(demand:list):
    highest_tot = []
    '''
       mon-fri [0:5]
       tues-sat [1:6]
       wed-sun [2:7]
       thurs-mon [3: next 0]
       fri-tues [4: next 1]
       sat-wed [5: next 2]
       sun-thurs [6: next 3]
    ''' 
    demand.extend(demand[0:3])
    
    idx = 0
    while idx < 7:
        highest_tot.append(sum(demand[idx:idx+5])) ## list of days with the total number of demand
        idx += 1
    print(highest_tot)
    
    
min_workers([4, 2, 4, 3, 5, 4, 6])