import yfinance as yf

amzn = yf.Ticker("AMZN")
info = amzn.get_info()

print("Name:", info["longName"])
print("Sector:", info["sector"])
print("Market Cap:", info["marketCap"])
print("current price:", info["currentPrice"])
print("dayhigh:", info["dayHigh"])

hist = amzn.history(period="1y")
print(hist.head())

balance_sheet = amzn.balance_sheet
income_stmt = amzn.income_stmt
cashflow = amzn.cashflow
print(balance_sheet.head())



import yfinance as yf
import matplotlib.pyplot as plt

stock = yf.Ticker("AMZN")
hist = stock.history(period="6mo")

plt.style.use('Solarize_Light2')
plt.figure(figsize = (10,6))

plt.plot(hist['Close'], label='Close', color='#00ff88')
plt.plot(hist['Open'], label='Open', color='#ff3388')
plt.plot(hist['High'], label='High', color='#00ccff')

plt.title( 'AMZN Stock Prices')
plt.tight_layout
plt.legend
plt.show()