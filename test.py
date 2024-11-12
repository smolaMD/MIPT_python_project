class Asset:
    """
    Represents a financial asset.
    """
    def __init__(self, name: str, quantity: int, price_per_unit: float):
        self.name = name
        self.quantity = quantity
        self.price_per_unit = price_per_unit

    def price(self):
        return self.quantity * self.price_per_unit
    
    """
    Calculates the total price of the asset based on its quantity and price per unit.

    """

    def __str__(self):
        return f'{self.name}: {self.quantity} units - {self.price_per_unit} per unit'

    def __eq__(self, other):
        if isinstance(other, Asset):
            return ((self.name == other.name) and (self.quantity == other.quantity) and (self.price_per_unit == other.price_per_unit))
        return False

class Stock(Asset):

    """
    Represents a stock asset, inheriting from Asset.
    """

    def __init__(self, name: str, quantity: int, price_per_unit: float):
        super().__init__(name, quantity, price_per_unit)

    def __str__(self):
        return f'{self.name}: {self.quantity} units - {self.price_per_unit} per unit'

class Obligation(Asset):
    """
    Represents a bond or obligation asset, inheriting from Asset.
    """

    def __init__(self, name: str, quantity: int, price_per_unit: float, interest_rate: float, maturity_date: float):
        super().__init__(name, quantity, price_per_unit)
        self.interest_rate = interest_rate
        self.maturity_date = maturity_date
    
    def total_interest(self):
        return self.price() * (self.interest_rate / 100)

    """
        Calculates the total interest earned from the obligation.
    """

class Currency(Asset):

    """
    Represents a currency asset, inheriting from Asset.
    """

    def __init__(self, name: str, quantity: int, price_per_unit: float):
        super().__init__(name, quantity, price_per_unit)


def convert(self, target_currency : Currency):
    exchange_rate = target_currency.price_per_unit / self.price_per_unit
    converted_amount = self.quantity * exchange_rate
    return converted_amount, target_currency.name

"""
Converts the amount of this currency to a target currency based on the exchange rate.
"""

class StockPortfolio:

    """
    Represents a portfolio of stocks.
    """

    def __init__(self):
        self.assets = []

    def add_asset(self, asset: Stock):
        for i in range(len(self.assets)):
            if self.assets[i].name == asset.name:
                self.assets[i].quantity += asset.quantity
                return
        self.assets.append(asset)

    """
    Adds a stock asset to the portfolio. If an asset with the same name already exists,
    updates its quantity.
    """
  
    def remove_asset(self, asset: Stock):
        for i in range(len(self.assets)):
            if self.assets[i].name == asset.name:
                if self.assets[i].quantity > asset.quantity:
                    self.assets[i].quantity -= asset.quantity
                elif self.assets[i].quantity < asset.quantity:
                    print("Not enough assets to sell")
                elif self.assets[i].quantity == asset.quantity:
                    self.assets.remove(asset)
                return
            
    """
    Removes a stock asset from the portfolio. If not enough assets are available,
    an error message is printed.
    """          

    def portfolio_price(self):
        portfolio_price = 0
        for i in range(len(self.assets)):
            portfolio_price += self.assets[i].quantity * self.assets[i].price_per_unit
        return portfolio_price
    
    """
        Calculates the total price of all assets in the portfolio.
    """

    def __str__(self):
        portfolio_str = "Your portfolio:\n"
        for i in range(len(self.assets)):
            portfolio_str += self.assets[i].__str__()
            portfolio_str += "\n"
        portfolio_str += f'Total price of portfolio: {round(self.portfolio_price(), 2)}'
        return portfolio_str