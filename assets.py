from tinkoff.invest import Client
from pandas import DataFrame
import logging
from tinkoff.invest.services import InstrumentsService
from tinkoff.invest.utils import quotation_to_decimal

TOKEN = 'token'

logging.basicConfig(format="%(asctime)s %(levelname)s:%(message)s", level=logging.DEBUG)
logger = logging.getLogger(__name__)
def GetFigi(ticker : str):
    with Client(TOKEN) as client:
        instruments: InstrumentsService = client.instruments
        tickers = []
        for method in ["shares", "bonds", "etfs", "currencies", "futures"]:
            for item in getattr(instruments, method)().instruments:
                tickers.append(
                    {
                        "ticker": item.ticker,
                        "figi": item.figi,
                    }
                )
        tickers_df = DataFrame(tickers)
        ticker_df = tickers_df[tickers_df["ticker"] == ticker]
        figi = ticker_df["figi"].iloc[0]
    return figi

def get_price_by_figi(figi_name):
    with Client(TOKEN) as client:
      request = client.market_data.get_order_book(figi=figi_name, depth=1)
      price_Q = request.last_price
      price = price_Q.units + price_Q.nano / (1e9)
      return price

SBER = get_price_by_figi(GetFigi("SBER")) # Сбер банк
AFLT = get_price_by_figi(GetFigi("AFLT")) # Аэрофлот
VKCO = get_price_by_figi(GetFigi("VKCO")) # ВК
MGNT = get_price_by_figi(GetFigi("MGNT")) # Магнит
YDEX = get_price_by_figi(GetFigi("YDEX")) # Яндек
GMKN = get_price_by_figi(GetFigi("GMKN")) # Норильский никель
OZON = get_price_by_figi(GetFigi("OZON")) # Озон
ROSN = get_price_by_figi(GetFigi("ROSN")) # Роснефть
AMZN = get_price_by_figi(GetFigi("AMZN")) # Аmazom
AAPL = get_price_by_figi(GetFigi("AAPL")) # Apple
MSFT = get_price_by_figi(GetFigi("MSFT")) # Microsoft
TSLA = get_price_by_figi(GetFigi("TSLA")) # Tesla
NVDA = get_price_by_figi(GetFigi("NVDA")) # NVIDIA
INTC = get_price_by_figi(GetFigi("INTC")) # Intel
NFLX = get_price_by_figi(GetFigi("NFLX")) # Netflix
MOEX = get_price_by_figi(GetFigi("MOEX")) # Московская биржа
VTBR = get_price_by_figi(GetFigi("VTBR")) # ВТБ
CSCO = get_price_by_figi(GetFigi("CSCO")) # Cisco Systems
ADBE = get_price_by_figi(GetFigi("ADBE")) # Adobe
PYPL = get_price_by_figi(GetFigi("PYPL")) # PayPal
TCSG = get_price_by_figi(GetFigi("TCSG")) # ТКС Холдинг