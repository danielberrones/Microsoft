import yfinance as yf

symbol = 'msft'
msft = yf.Ticker(symbol)

totalRevenue = msft.get_info()["totalRevenue"]

sep = "{:,}".format(totalRevenue)
print("totalRevenue\n", sep)

#totalRevenue
#192,557,006,848
