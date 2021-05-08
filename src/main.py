"""
This is the main module for our project.
"""
# import requestEquityDataAPI as EquityAPI
import makeEquityVectors as EV
import perceptron as tron

#-----------------------------------------------------------------------------
# path to alpha vantage API keys
#-----------------------------------------------------------------------------
# keypath = "apikey.key"
# mock_keypath = "mockkeys.key"


#-----------------------------------------------------------------------------
# list of companies to test
#-----------------------------------------------------------------------------
SP500_SYMBOLS = ['MMM', 'ABT', 'GOOGL', 'AMZN',
                 'MSFT', 'FB', 'AAPL', 'JPM', 'TSLA']

# SP500_SYMBOLS = ['JNJ', 'NFLX', 'NVDA', 'UNH', 'WFC', 'C', 'COST', 'QCOM', 'PFE',
                 # 'INTC', 'BAC', 'PG', 'DIS']


#-----------------------------------------------------------------------------
# parse all data for the given list of companies
#-----------------------------------------------------------------------------
# EquityAPI.requestEquityData(SP500_SYMBOLS, parser.getKeyList(keypath), DBUG=True)


"""
Next up, we use a perceptron to try to predict the last entry.
"""
csv_path = 'data/TimeSeries/AAPL.csv'
raw = EV.getEquityData(csv_path)
x, s, e = EV.convert2Vectors(raw)


w = tron.std_tron(e, x)
print(f"the weight vector is: {w}")
