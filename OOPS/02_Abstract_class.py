from abc import ABC,abstractmethod

class base(ABC):
    def __init__(self,price):
        self.price = price
    
    @abstractmethod
    def get_description():
        pass

class stocks(base):
    def __init__(self,Company,Ticker,price):
        super().__init__(price)
        self.Company = Company
        self.Ticker = Ticker

    def get_description(self):
        return f"{self.Ticker}: {self.Company} -- ${self.price}"

class bonds(base):

    def __init__(self,yields, description, duration, price):
        super().__init__(price)
        self.description = description
        self.duration = duration
        self.yields = yields

    def get_description(self):
        return f"{self.description}: {self.duration}'yr' : {self.price} : {self.yields}"
    

s1 = stocks("MSFT", 342.0, "Microsoft")
s2 = stocks("GOOG", 210.0, "Google")
s3 = stocks("META", 567.0, "Meta")

print(s1.get_description())
print(s2.get_description())
print(s3.get_description())

b1 = bonds(195.31, "30 year US treasury", 30, 4.38)
b2 = bonds(269.31, "20 year Securities", 20, 9.38)
b3 = bonds(155.31, "10 year US treasury", 10, 4.38)


print(b1.get_description())
print(b2.get_description())
print(b3.get_description())