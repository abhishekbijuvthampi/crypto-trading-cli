from data.market_data import MarketData
from binance.client import Client
from config.settings import API_KEY,API_SECRET
from execution.orders import Orders
from execution.account import Account
import pandas as pd

symbol = "BNBUSDT"
interval = "1h"
limit = 5

quantity = 0.1
signal = "BUY"

client = Client(
    API_KEY,
    API_SECRET,
    testnet=True
)

market = MarketData(client)
current_price = MarketData.crt_price(client,symbol)
order = Orders(client)
account = Account(client)

if signal == "BUY":
    result = order.market_buy(
        symbol="BTCUSDT",
        quantity=0.005
    )



print(account.show_balance("USDT"))
print(account.show_balance("BTC"))