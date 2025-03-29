import numpy as np
# import matplotlib.pyplot as plt

# def plot_peaks(prices, peaks):
#     plt.plot(prices, label="Stock Prices")
#     plt.scatter(peaks, prices[peaks], color='red', marker='o', label="Peaks")
#     plt.xlabel("Time")
#     plt.ylabel("Price")
#     plt.title("Stock Price Peaks")
#     plt.legend()
#     plt.show()

stock_prices = np.array([100, 102, 98, 105, 101, 107, 99, 110, 104, 103, 108])

def find_peak(prices,confirmed_peaks:list, min_dist:int):
    # base case => no more prices or not enough prices to form peaks
    if len(prices) < 3:
        return confirmed_peaks
    
    # init variables
    new_prices = prices
    new_peaks = confirmed_peaks
    sorted_prices = new_prices[:]
    sorted_prices.sort(reverse=True)
    
    # locate peak through iteration, greatest first
    for point in sorted_prices:
        # print(point)
        point_pos = new_prices.index(point)
        # print(point_pos)
        # validate max is a peak
        if (point_pos-1 >= 0) and (point_pos + 1 <= len(new_prices)-1):
            new_peaks.append(point_pos)
            
            # define range of points to remove from
            if point_pos - min_dist < 0:
                range_start = 0
            else:
                range_start = point_pos - min_dist
            if point_pos + min_dist > (len(new_prices) -1):
                range_end = len(new_prices)-1
            else:
                range_end = point_pos + min_dist
                
            range_remove = new_prices[range_start:range_end]
            
            input_prices = [ i for i in new_prices if i not in range_remove]
            
            result = find_peak(input_prices,new_peaks,min_dist)
            if result:
                return result
            
    return None
    

def find_local_peaks(prices, min_distance = 3):
    converted_prices = prices.tolist()
    return find_peak(converted_prices,[], min_distance)
    

print(find_local_peaks(stock_prices))