from data.market_data import MarketData
from binance.client import Client
from config.settings import API_KEY,API_SECRET
from execution.orders import Orders
from execution.account import Account
from cli import args, checkCMD
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

checkCMD(account)