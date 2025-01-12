from abc import ABC,abstractmethod
from dataclasses import dataclass

@dataclass()
class asset(ABC):
    price: float
    
    @abstractmethod
    def __lt__():
        pass

@dataclass()
class stocks(asset):
    Company: str
    Ticker: str 

    def __lt__(self,value):
        return self.price < value.price
  
@dataclass()
class bonds(asset):
    description: str
    duration: int
    yields: float 

    def __lt__(self,value):
        return self.yields < value.yields
    
stocklist = [
stocks("MSFT", 342.0, "Microsoft"),
stocks("GOOG", 210.0, "Google"),
stocks("META", 567.0, "Meta") ]

bondlist = [ bonds(195.31, "30 year US treasury", 30, 4.38),
             bonds(269.31, "20 year Securities", 20, 9.38),
             bonds(155.31, "10 year US treasury", 10, 4.38) ]

for s1 in stocklist:
    print(s1)

for b1 in bondlist:
    print(b1)

stocklist.sort();
bondlist.sort();

print()
print("After sorting")
print("-------------") 

for s1 in stocklist:
    print(s1)

for b1 in bondlist:
    print(b1)
