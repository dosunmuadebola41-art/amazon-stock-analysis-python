What is this Project about?
This project applies the basics of Python and uses a powerful library called y-finance for analysing stock data and I chose to do this for Amazon. 
Accessing Stock Data
I imported y-finance and accessed the amazon stock with the ticker name (AMZN). The library y-finance is used for downloading financial data on publicly traded companies. 
Accessing Company Information
Amazon’s company information is then accessed through the .info property, and this contains 100+ fields with company data, financials, and market metrics. 
Download Stock History
Stock History can be downloaded at different time intervals with the history function. This loads the data into a pandas Data Frame. We can also control the period and interval for the stock data, and we could also apply this to multiple stocks at once, which is the purpose of the download function, and includes the stocks we want in tickers list. 
Accessing financial reports
We can access quarterly and annual financial reports including balance sheet, income statement, and cashflow, and this loads the data into a pandas Data Frame. 
Visualising the data
We can then combine the stock data with matplotlib to create stock charts. 
