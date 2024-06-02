from pyscript import window
from pprint import pprint

pyfarm = window.pyfarmApp
textbox = pyfarm.findObjectByName("textbox")

class Farm: 
    def __init__(self): 
        self.pyfarm = window.pyfarmApp
        self._eggs_stock = self.pyfarm.getVariable("stock_eggs")
        self._corn_stock = self.pyfarm.getVariable("stock_corn")
        self._eggs_price = self.pyfarm.getVariable("price_eggs")
        self._corn_price = self.pyfarm.getVariable("price_corn")
        self._profit = 0

    @property
    def eggs_stock(self):
        return self._eggs_stock

    @property
    def eggs_price(self):
        return self._eggs_price
    
    @property
    def corn_stock(self):
        return self._corn_stock
    
    @property
    def corn_price(self):
        return self._corn_price
    
    @property
    def profit(self):
        return self._profit
    
    @profit.setter
    def profit(self, value):
        print("No cheatzies!")
    
    @eggs_stock.setter
    def eggs_stock(self, value):
        if type(value) != int:
            print("Stock must be a whole number")
            return 
        self.pyfarm.setVariable("stock_eggs", value)
        self._eggs_stock = value
    
    @eggs_price.setter
    def eggs_price(self, value):
        if type(value) not in [int, float]:
            print("Price must be a number")
            return
        self.pyfarm.setVariable("price_eggs", value)
        self._eggs_price = value

    @corn_stock.setter
    def corn_stock(self, value):
        if type(value) != int:
            print("Stock must be a whole number")
            return 
        self.pyfarm.setVariable("stock_corn", value)
        self._corn_stock = value

    @corn_price.setter
    def corn_price(self, value):
        if type(value) not in [int, float]:
            print("Price must be a number")
            return
        self.pyfarm.setVariable("price_corn", value)
        self._corn_price = value

    def sell_eggs(self, amount=1):
        if self.eggs_stock < amount:
            print("Not enough eggs in stock")
            return
        self.eggs_stock -= amount
        self._profit += self.eggs_price * amount
        self.update_profit()
        print(f"Sold {amount} egg(s) for ${self.eggs_price}")

    def sell_corn(self, amount=1):
        if self.corn_stock < amount:
            print("Not enough corn in stock")
            return
        self.corn_stock -= amount
        self._profit += self.corn_price * amount
        self.update_profit()
        print(f"Sold {amount} corn for ${self.corn_price}")

    def update_profit(self):
        self.pyfarm.setVariable("profit", self._profit)

farm = Farm()

