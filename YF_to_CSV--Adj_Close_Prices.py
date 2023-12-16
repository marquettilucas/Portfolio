##### this code will generate a CSV file from a given assets and date range inputed

#import libs
import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
import datetime as dt


# input stocks and organize into a List Object, 
tickers = [item for item in input("Enter the stock tickers, for portfolio (space them only) : ").split()]   

yf.pdr_override()

# define a date range, 
time = int(input("Enter the date range in Years "))

end = dt.datetime.now()
start = end - dt.timedelta(days = 365*time)
file_name = input("Enter the file name ")# + ".csv"

#obtain data from Yfinance
df = pdr.get_data_yahoo(tickers, start = start, end = end)

#extract Ajusted Close prices only:
Adj_close_df = df['Adj Close']

#export DataFrame to CSV file
Adj_close_df.to_csv(file_name)
