from abc import ABC,abstractmethod

class asset(ABC):
    def __init__(self,price):
        self.price = price
    
    @abstractmethod
    def get_description():
        pass

class stocks(asset):
    def __init__(self,Ticker,price, Company):
        super().__init__(price)
        self.Company = Company
        self.Ticker = Ticker

    def get_description(self):
        return f"{self.Ticker}: {self.Company} -- ${self.price}"
    
    def __str__(self):
        return f"{self.Ticker}: {self.Company} -- ${self.price}"
    
    def __le__(self,value):
        if not isinstance(value,stocks):
            raise ValueError("Can't compare stock to non stock")
        
        return (self.price <= value.price)

    def __lt__(self,value):
        if not isinstance(value,stocks):
            raise ValueError("Can't compare stock to non stock")
        
        return (self.price < value.price)

class bonds(asset):

    def __init__(self,yields, description, duration, price):
        super().__init__(price)
        self.description = description
        self.duration = duration
        self.yields = yields

    def get_description(self):
        return f"{self.description}: {self.duration}'yr' : {self.price} : {self.yields}"
    
    def __str__(self):
        return f"{self.description}: {self.duration}'yr' : {self.price} : {self.yields}"

    
    def __lt__(self,value):
        if not isinstance(value,bonds):
            raise ValueError("value is not a bond object")
        return (self.yields < value.yields)
    
stocklist = [
stocks("MSFT", 342.0, "Microsoft"),
stocks("GOOG", 210.0, "Google"),
stocks("META", 567.0, "Meta") ]

for s1 in stocklist:
    print(s1.get_description())

bondlist = [ bonds(195.31, "30 year US treasury", 30, 4.38),
             bonds(269.31, "20 year Securities", 20, 9.38),
             bonds(155.31, "10 year US treasury", 10, 4.38) ]

for b1 in bondlist:
    print(b1.get_description())

stocklist.sort();
bondlist.sort();

print()
print("After sorting")
print("-------------")
for s1 in stocklist:
    print(s1)
    
for b1 in bondlist:
    print(b1)