from tinkoff.invest import Client
from main import Asset, StockPortfolio

TOKEN = 't.WfWkdeacZcm_gc3LD65QnzaA6EjmaB9netijeL6_SLC8r-m8H2l7wwzPpc42fA6q5QGPo50HEv8XDShwQ8Aynw'

def RealAssests(figi_name):
    with Client(TOKEN) as client:
      r = client.market_data.get_order_book(figi=figi_name, depth=1)
      price_Q = r.last_price
      price = price_Q.units + price_Q.nano / (1e9)
      return price

SBER = RealAssests('BBG004730N88') # Сбер банк
AFLT = RealAssests('BBG004S683W7') # Аэрофлот
#VKCO = RealAssests('VKCO', 'BBG01JPFQH64', quantity) # ВК
MGNT = RealAssests('BBG004RVFCY3') # Магнит
#YDEX = RealAssests('YDEX', 'BBG01NSDQL68', quantity) # Яндек
GMKN = RealAssests('BBG004731489') # Норильский никель
