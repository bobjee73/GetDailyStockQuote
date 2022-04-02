from nsetools import Nse
from pprint import pprint

my_stocks = [
"bpcl",
"britannia",
"hdfc",
"heromotoco",
"HINDUNILVR",
"INFY",
"irctc",
"itc",
"lt",
"maruti",
"mphasis",
"nmdc",
"ntpc",
"RELIANCE",
"SHRIRAMCIT",
"SRTRANSFIN",
"tatachem",
"TATACONSUM",
"tatapower",
"tatasteel",
"tcs" ]

nse = Nse()

# pprint(my_stocks)

print("%20s %9s %9s %9s %9s %10s %9s %10s %10s %50s" % ("Stock", "LTP", "Low", "High", "52wLow", "", "52wHigh", "Ex Date", "Rec Date", "Purpose"))
print("-"*20, "-"*9, "-"*9, "-"*9, "-"*9, "-"*10, "-"*9, "-"*10, "-"*10, "-"*50,)
for stock in my_stocks:
    stock_quote = nse.get_quote(stock.upper())
    stock_symbol = stock_quote['symbol']
    stock_ltp = stock_quote['closePrice']
    stock_low = stock_quote['dayLow']
    stock_high = stock_quote['dayHigh']
    low52 = round(stock_quote['low52'])
    high52 = round(stock_quote['high52'])
    # hi52_minus_lo52 = high52 - low52
    # close_minus_lo52 = stock_ltp - low52
    close_to_low52_percentage = round((stock_ltp - low52)/(high52 - low52) * 10)
    close_to_low52 = ""
    for i in range(0,10):
        if i == close_to_low52_percentage:
            close_to_low52 += '.'
        else:
            close_to_low52 += '_'
    exdate = stock_quote['exDate']
    record_date = stock_quote['recordDate']
    purpose = stock_quote['purpose']
    print("%20s %9s %9s %9s %9s %10s %9s %10s %10s %50s" % (stock_symbol, stock_ltp, stock_low,
                                             stock_high, low52, close_to_low52, high52,
                                             exdate, record_date, purpose))
"""
scful = nse.get_quote("SHRIRAMCIT")
pprint(scful)
"""
