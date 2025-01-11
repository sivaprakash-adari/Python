#   This program is to implement the stock class
#


class Stock:
    def __init__(self,Ticker, Price, Company):
        self.Ticker = Ticker
        self.Price = Price
        self.Company = Company

    def get_description(self):
        return self.Ticker + ": " + self.Company + " -- $" + str(self.Price)
    
    def get_description2(self):
        return f"{self.Ticker}: {self.Company} -- ${self.Price}";
    

s1 = Stock("MSFT", 342.0, "Microsoft")
s2 = Stock("GOOG", 210.0, "Google")
s3 = Stock("META", 567.0, "Meta")

print(s1.get_description())
print(s2.get_description())
print(s3.get_description())

print("\nfstring method")
print("---------------")
print(s1.get_description2())
print(s2.get_description2())
print(s3.get_description2())