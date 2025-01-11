
class book:
    def __init__(self,title,price,auth):
        self.title = title
        self.price = price
        self.author = auth 

    def get_book_details(self):
        _name = self.author.get_name()
        return f"Title : {self.title} Author : {_name} Price : ${self.price}"

class Author:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def get_name(self):
        return f"{self.firstname} {self.lastname}"

auth1 = Author( "Robert" , "Keyosaki")
auth2 = Author( "James" , "Clear")

b1 = book("RichDad PoorDad", 200, auth1)

b2 = book("Atomic Habits", 300, auth2)

print(b1.get_book_details())
print(b2.get_book_details())