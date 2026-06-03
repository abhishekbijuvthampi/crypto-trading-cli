class Account:
    def __init__(self, client):
        self.client = client

    def show_log(self, symbol):
        return self.client.get_mytrades(
            symbol = symbol
            )
    
    def show_asset(self, asset):
        return(self.client.get_asset_balance(
            asset = asset
            ))