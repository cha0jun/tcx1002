price_list = {
    'pear' : [(1, 1.0), (5, 3.9), (10, 6.9)],
    'milk' : [(1, 2.8), (2, 4.9)],
    'rice 5kg' : [(1, 15.95)]
}

def calc_total(items:list):
    output = {
        'total' : 0,
        'items' : []
    }
    for x in items:
        quantity = x[1]
        price = 0
        prices = price_list[x[0]][::-1]
        idx = 0
        while quantity > 0:
            if quantity >= prices[idx][0]:
                quantity = quantity - prices[idx][0]
                price = price + prices[idx][1]
            else:
                idx += 1
            
        output['total'] += price
        output['items'] += [(x[0],x[1],price)]
    return output
        
print(calc_total([('pear', 16), ('milk', 3), ('rice 5kg', 1)]))