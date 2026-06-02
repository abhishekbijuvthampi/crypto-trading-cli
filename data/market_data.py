import pandas as pd

class MarketData:
    def __init__(self, client):
        self.client = client

    def get_klines(self, 
                   symbol = "BTCUSDT", 
                   interval = "1h", 
                   limit=100):
        
        return self.client.get_klines(
            symbol = symbol,
            interval = interval,
            limit = limit
        )
    
    def crt_price(self, symbol):
        crypto_info = self.get_all_tickers()
        df = pd.DataFrame(crypto_info)

        #curent market price of symbol
        current_price = df[df["symbol"] == symbol]

        return current_price
    
    def get_acc_asset(self):
        asset_bal = self.get_asset_balance()
        df = pd.DataFrame(asset_bal)
        
        return df