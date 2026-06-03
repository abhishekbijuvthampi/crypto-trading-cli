class Orders:

    def __init__(self, client):
        self.client = client

    def market_buy(self, symbol, quantity):

        order = self.client.order_market_buy(
            symbol=symbol,
            quantity=quantity)

        return order
    
    def market_sell(self, symbol, quantity):

        order = self.client.order_market_sell(
            symbol = symbol,
            quantity = quantity)

        return order
    
    def limit_buy(self, symbol, quantity, price):
        order = self.client.order_limit_buy(
            symbol= symbol,
            quantity=quantity,
            price=price)

        return order
        
    def limit_sell(self,symbol, quantity, price):
        order = self.client.order_limit_sell(
            symbol= symbol,
            quantity=quantity,
            price=price)

        return order