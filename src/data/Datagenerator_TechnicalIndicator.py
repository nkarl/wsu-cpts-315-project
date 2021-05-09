from alpha_vantage.techindicators import TechIndicators
key = 'M4JP31006H3PKZ8T'
symbol = input('Ticker : ')
outputsize = 'compact'
interval =input('Interval- 1min,5min,15min,30min,60min,daily,weekly,monthly : ')
time = input('Time Period : ')
tech_indi = input('Technical Indicator- SMA,EMA,VWAP,MACD,Stochastic Oscillator,RSI,Bollinger bands :')
ti = TechIndicators(key,output_format='pandas')
if tech_indi == 'SMA':
    state = ti.get_sma(symbol, interval=interval, time_period=time, series_type='close')[0]
elif tech_indi == 'EMA':
    state = ti.get_ema(symbol, interval=interval, time_period=time, series_type='close')[0]
elif tech_indi == 'VWAP':
    state = ti.get_vwap(symbol, interval=interval)[0]
elif tech_indi == 'MACD':
    state = ti.get_macd(symbol, interval=interval, series_type='close')[0]
elif tech_indi == 'Stochastic Oscillator':
    state = ti.get_stoch(symbol, interval=interval)[0]
elif tech_indi == 'RSI':
    state = ti.get_rsi(symbol, interval=interval, time_period=time, series_type='close')[0]
elif tech_indi == 'Bollinger bands':
    state = ti.get_bbands(symbol, interval=interval, time_period=time, series_type='close')[0]
else:
    print('Wrong Entry')
print(state)