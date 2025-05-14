from abc import ABC, abstractmethod

class Asset(ABC):
    def __init__(self, price):
        self.price = price

    @abstractmethod
    def get_description(self):
        pass

class Stock(Asset):
    def __init__(self, ticker, price, company):
        super().__init__(price)
        self.ticker = ticker
        self.company = company

    def get_description(self):
        return f"{self.ticker}: {self.company} -- ${self.price}"
    
class Bond(Asset):
    def __init__(self, price, description, duration, yieldamt):
        super().__init__(price)
        self.description = description
        self.duration = duration
        self.yieldamt = yieldamt

    def get_description(self):
        return f"{self.description}: {self.duration}yr : ${self.price} : {self.yieldamt}%"
    
try:
    ast = Asset(100.0)
except:
    print("Failed Instantiation!")

msft = Stock("MSFT", 342.0, "Microsoft Corp")

us30yr = Bond(95.32, "US 30 Year Treasury", 30, 4.38)

print(msft.get_description())
print(us30yr.get_description())