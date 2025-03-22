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

class AdvancedOrder(Order):
    def __init__(self):
        super().__init__()
        self._collection_time = ''
    
    @property
    def collection_time(self):
        return self._collection_time
    
    @collection_time.setter
    def collection_time(self, time:str):
         self._collection_time = time
        
    def checkout(self):
        return super().checkout() + (self.collection_time,)
        
        

class DeliveryOrder(AdvancedOrder):
    def __init__(self):
        super().__init__()
        self._address = ''
    
    @property
    def address(self):
        return self._address
    
    @address.setter
    def address(self, new_address:str):
        self._address = new_address
        
    def checkout(self):
        return super().checkout() + (self.address,)
        


o = DeliveryOrder()
o.add_item("Beansprout")
o.add_item("Chicken")
o.add_item("Rice")
o.collection_time = "19/12/2024 12:15"
o.address = "123 ABC Street"

print(o.checkout())
o_advanced_104 = AdvancedOrder()

print(o_advanced_104.checkout())
