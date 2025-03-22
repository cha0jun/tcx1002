from datetime import datetime

next_book_id = 1
def increment_book_id(): #use this function to maintain global state of next_book_id
    global next_book_id
    next_book_id += 1

class Book:
    def __init__(self,title:str, author:str):
       self._id = next_book_id
       increment_book_id()
       self.title = title
       self.author = author
       self._status = 'available'
       
    def __str__(self):
        return f'Book ID: {self._id}, Title: {self.title}, Author: {self.author}, status: {self.status}'
    
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self,new_status:str):
        status_ls = ['available', 'on loan', 'on maintenance']
        try:
            if not new_status:
                raise Exception('Status is empty')
            elif new_status not in status_ls:
                raise Exception('Invalid status')
            elif self.status == 'available':
                if new_status == 'available':
                    raise Exception()
            elif self.status == 'on loan':
                if new_status == 'on maintenance':
                    raise Exception()
            else: ## on maintenance
                if new_status == 'on loan':
                    raise Exception()
        except:
            raise Exception('Invalid status change')
        self._status = new_status
              
    
class Borrow:
    def __init__(self,name:str,book_obj:str):
        if book_obj.status != 'available':
            raise Exception('Can not borrow book which is not available')
        self.borrower = name
        self._book = book_obj
        self.b_date = datetime.now()
        self.r_date = None
        book_obj.status = 'on loan'
        
    def return_book(self):
        self.r_date = datetime.now()
        self._book.status = 'available'
        
    def __str__(self):
        return f'Borrower: {self.borrower}, Book ID: {self._book._id}, Borrow DateTime: {self.b_date}, Return DateTime: {self.r_date}'

# Do NOT change the following testcases
book1 = Book('Intro to Python', 'Alice')
borrow1 = Borrow('Charlie', book1)
test1 = str(book1)
print("1", test1)

try:
  book1.status = 'on maintenance'
except Exception as e:
  test2 = str(e)
  print("2", test2)

borrow1.return_book()
test3 = str(book1)
print("3", test3)

book1.status = 'on maintenance'
test4 = str(book1)
print("4", test4)

try:
  borrow2 = Borrow('Denny', book1)
except Exception as e:
  test5 = str(e)
  print("5", test5)
