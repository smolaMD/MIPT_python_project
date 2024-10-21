from tinkoff.invest import Client
from main import Asset, StockPortfolio

TOKEN = 't.WfWkdeacZcm_gc3LD65QnzaA6EjmaB9netijeL6_SLC8r-m8H2l7wwzPpc42fA6q5QGPo50HEv8XDShwQ8Aynw'

def RealAssests(name, figi_name, quantity):
    with Client(TOKEN) as client:
      r = client.market_data.get_order_book(figi=figi_name, depth=1)
      price_Q = r.last_price
      price = price_Q.units + price_Q.nano / (1e9)
      return Asset(f'{name}', quantity, price)
    
quantity = 10
SBER = RealAssests('SBER', 'BBG004730N88', quantity)

portfolio = StockPortfolio()
portfolio.add_asset(SBER)
print(portfolio.__str__())
