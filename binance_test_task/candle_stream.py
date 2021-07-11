import os

from binance_test_task.moving_average import moving_average


class candle_stream():
    """
    Get candles of BTC/USDT, ETH/USDT, BNB/BTC
    For more info https://github.com/binance/binance-spot-api-docs/blob/master/web-socket-streams.md#klinecandlestick-streams
    """

    def __init__(self, binance_manager, client, subscribed_symbol, frequency, window_size = 5):
        self.bm = binance_manager
        self.client = client
        self.symbol = subscribed_symbol
        self.freq = frequency
        self.status = False
        self.window_size = window_size

    async def subscribe_symbol(self):
        # start kline sockets
        ts = self.bm.kline_socket(self.symbol)
        # then start receiving messages
        async with ts:
            ma = []
            while True:
                res = await ts.recv()
                # print(res)
                path = f"./output/{self.symbol}_price.txt"
                mode = 'a' if os.path.exists(path) else 'w'
                with open(path, mode) as f:
                    f.writelines(str([res['E'], res['s'], res['k']]) + "\n")
                m_avg = moving_average(self.window_size)
                m_avg.add_value(ma, res['k']['c'])
                if m_avg.calculate(ma) is not None:
                    print(f'Moving average for `{self.symbol}`  is {m_avg.calculate(ma)}')
                await self.client.close_connection()