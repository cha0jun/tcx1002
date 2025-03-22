import random

class Payment:
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return f'{self.amount}'
    
    @property
    def details(self):
        return self.amount
    
class EPayment(Payment):
    def __init__(self, refer_num, amount):
        super().__init__(amount)
        self.ref_num = refer_num

    def __str__(self):
        return f'({self.ref_num},{self.amount})'

    @property
    def details(self):
        return (self.ref_num,self.amount)

class Order:
    def __init__(self, item, total_price, customer, address, online:bool = True):
        if total_price < 0:
            raise Exception('Invalid total price')
        self.item = item
        self.total_price = total_price
        self.customer = customer
        self._address = address
        code = str(random.randint(0,999999))
        if len(code) < 6:
            code.ljust(6-len(code),"0")
        self.delivery_code = code
        self.delivery_status = 'pending'
        self.payment_status = 'pending'
        self.__amount_paid = 0
        self.payments = []
        if online:
            self.deliver(self.delivery_code)
            
    @property
    def address(self):
        return self._address
    
    @address.setter
    def address(self, new_address):
        self._address = new_address
    
    @property
    def status(self):
        return f'item: {self.item}, total: {self.total_price}, customer: {self.customer}, address: {self.address}, delivery: {self.delivery_status}, payment: {self.payment_status} {self.payments}'
    
    
    def pay(self, payment:Payment):
        if payment.amount <= 0:
            raise Exception('Payments made must be greater than 0.')
        self.payments.append(payment.details)
        self.__amount_paid = self.__amount_paid + payment.amount
        if self.__amount_paid >= self.total_price:
            self.payment_status = 'paid'
        else:
            self.payment_status = 'partially'
        

    def deliver(self, code):
        if self.delivery_code == code:
            self.delivery_status = 'delivered'
        else:
            raise Exception('Delivery not found')



# Do not change the following, they are for grading purpose
o1 = Order('laptop', 2000.0, 'Alice', '123 ABC Street')
o1.pay(EPayment('1234567', 1000.0))
o1.pay(Payment(1000.0))
o1.address = '321 ABC Street'

o2 = Order('Python programming', 35.0, 'Bob', '', online=True)
o2.pay(Payment(15.0))