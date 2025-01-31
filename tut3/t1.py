def moving_average(prices:list, window_size:int):
    res = []
    for idx in range(len(prices[window_size:])+1):
        avg = (sum(prices[idx:window_size+idx]) / window_size)
        res.append(round(avg,2))
    return res
        
print(moving_average([50, 52, 51, 53, 55, 56, 58,60],3))