docker rmi -f binance & docker build --rm -t binance .

rem docker run --name binance_cont -t -i --rm binance

rem ------
rem for test-case, when CMD and ENTRY are disabled in Dockerfile - then go to live bash session
docker run --name binance_cont -t -i --rm binance bash