from data.market_data import MarketData
from binance.client import Client
from config.settings import API_KEY,API_SECRET
from execution.orders import Orders
from execution.account import Account
from cli import args, checkCMD
import pandas as pd

try:
    client = Client(
        API_KEY,
        API_SECRET,
        testnet=True
    )
except Exception as e:
    print(f"Error: {e}")

market = MarketData(client)
order = Orders(client)
account = Account(client)



info = checkCMD(account, order)