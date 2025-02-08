import csv

def stock_analysis(file_path:str, percentagePoint:float):
    window_size= 4
    ori = {}
    with open(file_path,'r') as file:
        reader = csv.reader(file)
        next(reader, None)
        for x in reader:
            if x[0] not in ori.keys():
                ori[x[0]] = []
            ori[x[0]].append(x[1:])
    res = {}
    for key in ori:
        if key not in res.keys():
            res[key] = []
            ls = ori[key][::-1]
            for idx in range(len(ls[window_size:])):
                if ((float(ls[idx][2])-float(ls[idx+window_size][1]))/float(ls[idx][2])) > percentagePoint:
                    res[key].append((ls[idx][0],float(ls[idx][2]),ls[idx+window_size][0],float(ls[idx+window_size][1])))
    return res
            
    
            
        
    
            
stock_analysis('stocks_data.csv', 0.03)