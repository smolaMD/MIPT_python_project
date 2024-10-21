class Asset:
    def __init__(self, name, quantity, price_per_unit):
        self.name = name
        self.quantity = quantity
        self.price_per_unit = price_per_unit
    
    def price(self):
        return self.quantity * self.price_per_unit
    
    def __str__(self):
        return f'{self.name}: {self.quantity} units - {self.price_per_unit} per unit'
    
    def __eq__(self, other):
        if isinstance(other, Asset):
            return ((self.name == other.name) and (self.quantity == other.quantity) and (self.price_per_unit == other.price_per_unit))
        return False
    
class StockPortfolio:

    def __init__(self):
        self.assets = []

    def add_asset(self, asset: Asset):
        for i in range(len(self.assets)):
            if self.assets[i].name == asset.name:
                self.assets[i].quantity += asset.quantity
                return
        self.assets.append(asset)
        
    def remove_asset(self, asset: Asset):
        for i in range(len(self.assets)):
            if self.assets[i].name == asset.name:
                if self.assets[i].quantity > asset.quantity:
                    self.assets[i].quantity -= asset.quantity
                elif self.assets[i].quantity < asset.quantity:
                    print("Not enough assets to sell")
                elif self.assets[i].quantity == asset.quantity:
                    self.assets.remove(asset)
                return
        print("No asset in portfolio")

    def portfolio_price(self):
        portfolio_price = 0
        for i in range(len(self.assets)):
            portfolio_price += self.assets[i].quantity * self.assets[i].price_per_unit
        return portfolio_price

    def __str__(self):
        portfolio_str = "Your portfolio:\n"
        for i in range(len(self.assets)):
            portfolio_str += self.assets[i].__str__()
            portfolio_str += "\n"
        portfolio_str += f'Total price of portfolio: {self.portfolio_price()}'
        return portfolio_str
