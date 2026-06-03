class Orders:

    def __init__(self, client):
        self.client = client

    def market_buy(self, symbol, quantity):

        order = self.client.order_market_buy(
            symbol=symbol,
            quantity=quantity)

        return(order)
    
    def market_sell(self, symbol, quantity):

        order = self.client.order_market_sell(
            symbol = symbol,
            quantity = quantity)

        return(order)