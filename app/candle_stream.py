import os
import logging
from app.moving_average import moving_average


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
        output_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                      "output")
        logging.basicConfig(filename='./logs/candle_stream.log', level=logging.INFO)
        async with ts:
            ma = []
            while True:
                res = await ts.recv()
                logging.info(res)

                if not os.path.exists(output_dir):
                    os.makedirs(output_dir)

                path = f"{output_dir}/{self.symbol}_price.txt"
                with open(path, 'a') as f:
                    f.writelines(str([res['E'], res['s'], res['k']]) + "\n")
                m_avg = moving_average(window_size=self.window_size)
                m_avg.add_value(ma, res['k']['c'])
                if m_avg.calculate(ma) is not None:
                    logging.info(f'Moving average for `{self.symbol}` is {m_avg.calculate(ma)}')
                    print(f'Moving average for `{self.symbol}` is {m_avg.calculate(ma)}')
                await self.client.close_connection()