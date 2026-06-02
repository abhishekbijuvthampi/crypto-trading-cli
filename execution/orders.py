class Orders:

    def __init__(self, client):
        self.client = client

    def market_buy(self, symbol, quantity):

        order = self.order_market_buy(symbol,quantity)

        return order
    
    def market_sell(self, symbol, quantity):

        order = self.order_market_sell(symbol,quantity)

        return order