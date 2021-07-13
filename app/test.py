import os
import asyncio
from binance import AsyncClient, BinanceSocketManager
from app.candle_stream import candle_stream
from app.config import settings


async def main():
    client = await AsyncClient.create()
    bm = BinanceSocketManager(client)

    task1 = candle_stream(bm, client, 'BTCUSDT', settings.frequency, settings.windows_size)
    task2 = candle_stream(bm, client, 'ETHUSDT', settings.frequency, settings.windows_size)
    task3 = candle_stream(bm, client, 'BNBBTC', settings.frequency, settings.windows_size)

    asyncio.create_task(task1.subscribe_symbol())
    asyncio.create_task(task2.subscribe_symbol())
    asyncio.create_task(task3.subscribe_symbol())

    await asyncio.sleep(10)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())

output_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                          "output")

for symbol in settings.subscribed_symbols.split(","):
    assert os.path.exists(f"{output_dir}/{symbol}_price.txt")
