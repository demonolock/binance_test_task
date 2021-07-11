class moving_average():
    """
    Get candles of BTC/USDT, ETH/USDT, BNB/BTC
    For more info https://github.com/binance/binance-spot-api-docs/blob/master/web-socket-streams.md#klinecandlestick-streams
    """

    def __init__(self, window_size = 5):
        self.window_size = window_size

    def calculate(self, ma):
        if len(ma) == self.window_size:
            return sum(ma)/ len(ma)
        else:
            return None

    def add_value(self, ma, value):
        if len(ma) == self.window_size:
            ma.pop(0)
            ma.append(float(value))
        else:
            ma.append(float(value))