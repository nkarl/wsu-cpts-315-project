

from alpha_vantage.timeseries import TimeSeries
key = 'M4JP31006H3PKZ8T'
outputsize = 'compact'
symbol = input('Ticker : ')
typ = input('Data type- "daily", "weekly", "monthly", "interval" : ')
ts = TimeSeries(key,output_format='pandas')
if typ == 'daily':
    state = ts.get_daily_adjusted(symbol,outputsize=outputsize)[0]
elif typ == 'weekly':
    state = ts.get_weekly_adjusted(symbol)[0]
elif typ == 'monthly':
    state = ts.get_monthly_adjusted(symbol)[0]
elif typ == 'interval':
    interval = input('Interval-1min, 5min, 15min, 30min, 60min : ')
    state = ts.get_intraday(symbol, interval=interval, outputsize=outputsize)[0]
else:
    print('Wrong input given by the user')
print(state)


