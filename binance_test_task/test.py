import os
import asyncio
from binance import AsyncClient, BinanceSocketManager
from binance_test_task.candle_stream import candle_stream

if __name__ == "__main__":
    async def main():
        client = await AsyncClient.create()
        bm = BinanceSocketManager(client)

        task1 = candle_stream(bm, client, 'BTCUSDT', '1min', window_size=3)
        task2 = candle_stream(bm, client, 'ETHUSDT', '1min', window_size=3)
        task3 = candle_stream(bm, client, 'BNBBTC', '1min', window_size=3)

        asyncio.create_task(task1.subscribe_symbol())
        asyncio.create_task(task2.subscribe_symbol())
        asyncio.create_task(task3.subscribe_symbol())

        await asyncio.sleep(10)


    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

    assert os.path.exists(f"./output/BNBBTC_price.txt")
    assert os.path.exists(f"./output/BTCUSDT_price.txt")
    assert os.path.exists(f"./output/ETHUSDT_price.txt")
