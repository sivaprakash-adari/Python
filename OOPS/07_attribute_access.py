
class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price
        self.discount = 0.1

    def __str__(self):
        return f"{self.title}, {self.author}, ${self.price}"
    
    def __getattribute__(self,name):
        if name == "price":
            p = super().__getattribute__("price")
            d = super().__getattribute__("discount")
            return (p - p*d)
        else:
            return super().__getattribute__(name)
        
    def __setattr__(self,name,value):
        if name == "price":
            if type(value) is not float:
                raise ValueError("assinged should be floating value")
        return super().__setattr__(name,value)

    def __call__(self, price):
        self.price = price
        
b1 = Book("RichDad PoorDad", "Robert", 200.0)
b2 = Book("Atomic Habits", "James", 300.0)

print(b1)
print(b2)

b2.price = 500.0

print(b2)
b2(700.0)
print(b2)