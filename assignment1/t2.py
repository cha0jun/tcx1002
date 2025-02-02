def find_highest_window(demand:list):
    demandlist = [] ## create a copy to prevent state change of original input
    demandlist.extend(demand)
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
    demandlist.extend(demandlist[0:3])
    idx = 0
    while idx < 7:
        highest_tot.append(sum(demandlist[idx:idx+5])) ## list of total demand of each 5 day window
        idx += 1  
    position = highest_tot.index(max(highest_tot))
    return position


def min_workers(demand:list):
    worker_list = []
    worker_count = 0
    total_demand = sum(demand)
    
    while total_demand > 0:
        curr = find_highest_window(demand)
        worker_list.append(curr)
        worker_count += 1
        for days in range(5): ## loop to reduce demand
            idx = days + curr
            if idx > 6:
                idx = idx - 7
            if demand[idx] > 0:
                val = demand[idx] - 1
                demand[idx] = val
        total_demand = sum(demand)
        
    return (worker_count, worker_list)
    
min_workers([4, 2, 4, 3, 5, 4, 6])
        
    
    
