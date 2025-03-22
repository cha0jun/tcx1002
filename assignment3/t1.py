# this global variable represents the last order number
# For any new order, increase this number, eg the new order no will be 103
last_order_num = 102

def increment_order_num():
    global last_order_num
    last_order_num += 1

menu = {
    "Beansprout": 1.00,
    "Chicken": 2.50,
    "Beef": 3.00,
    "Rice": 0.70,
}

class Order:
    def __init__(self):
        increment_order_num()
        self._order_num = last_order_num
        self.items = []
        self.total_price = 0.0
    
    def add_item(self, item_name:str):
        self.items.append(item_name)
        self.total_price += round(menu[item_name],2)
        

    def remove_item(self, item_name:str):
        try:
            self.items.remove(item_name)
            self.total_price -= menu[item_name]
        except:
            raise Exception('Item not found in order')
        
    def checkout(self):
        return (self._order_num, self.items, self.total_price, "https://pay.onlinebank.com.sg/123456/"+str(self._order_num))


o = Order()
o.add_item("Beansprout")
o.add_item("Chicken")
o.add_item("Rice")

print(o.checkout())
print(o.total_price)
