"""
From the Alpha Vantage API, we are going to use Intraday (Extended history)
for our data set. Within this set (containing over 2 million minute-points),
we will use the 60-minute-points instead to cut down on the size of our input.
"""
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.sectorperformance import SectorPerformances
from pprint import pprint

from matplotlib import pyplot

MY_API_KEY = 'M4JP31006H3PKZ8T'


# getting the slice/snapshot of monthly data over 2 years
#-----------------------------------------------------------------------------
# each snapshot is 30-day.
slices = []
for y in range(1, 3):
    year = ""
    year += "year" + str(y)
    for i in range(1,13):
        month = ""
        month += year + "month" + str(i)
        slices.append(month)

SP500_SYMBOLS = ['MMM', 'ABT', 'GOOGL', 'AMZN', 'MSFT']


# building the dataset
#-----------------------------------------------------------------------------
DATA = dict()

def getData(symbol):
    ts = TimeSeries(key=f"{MY_API_KEY}", rapidapi=True,
                    output_format='pandas',
                    indexing_type='date')
    ts = TimeSeries(key=f"{MY_API_KEY}", output_format='pandas',
                    indexing_type='date')

    tsdata, tsmeta_data = ts.get_intraday(
                    symbol='MSFT', interval='1min', outputsize='full')


    ti = TechIndicators(key=f"{MY_API_KEY}", output_format='pandas',
                        indexing_type='data')
    tidata, timeta_data = ti.get_bbands(symbol='MSFT', interval='60min',
                                    time_period=60)


    sp = SectorPerformances(key=f"{MY_API_KEY}", output_format='pandas')
    spdata, spmeta_data = sp.get_sector()
    spdata['Rank A: Real-Time Performance'].plot(kind='bar')
