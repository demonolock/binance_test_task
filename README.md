# Подсчет скользящего среднего для свечек из binance

В `.env` задаются параметры приложения
```
WINDOW_SIZE=3 \\ размер окна для скользящего среднего
SUBSCRIBED_SYMBOLS=BTCUSDT,ETHUSDT,BNBBTC \\ список для подписки 
FREQUENCY=1min \\ частота
```

В moving_average реализована логика подсчета скользящего среднего.
В candle_stream реализовано подключение к binance и выгрузка нужных данных.
Более подробную информацию по API можно найти [тут.](https://github.com/binance/binance-spot-api-docs/blob/master/web-socket-streams.md#klinecandlestick-streams)
 
В папку `output` выгружаются данные по подпискам. 
В папку `logs` логи приложения.
