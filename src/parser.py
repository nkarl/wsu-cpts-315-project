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


# # getting the slice/snapshot of monthly data over 2 years
# #-----------------------------------------------------------------------------
# # each snapshot is 30-day.
# slices = []
# for y in range(1, 3):
    # year = ""
    # year += "year" + str(y)
    # for i in range(1,13):
        # month = ""
        # month += year + "month" + str(i)
        # slices.append(month)


# building the dataset
#-----------------------------------------------------------------------------
DATA = dict()

def writeData(path, data):
    """
    write stock data to csv.
    """
    with open(path, 'w') as write_csvfile:
        writer = csv.writer(write_csvfile, dialect='csv')
        for row in data:
            writer.writerow(row)


def getData(equity):
    """
    parse data for a given stock symbol.

    :param equity (panda series): TimeSeries data and TechIndicators pandaframe.
    """
    # ts = TimeSeries(key=f"{MY_API_KEY}", rapidapi=True, output_format='pandas', indexing_type='date')
    ts = TimeSeries(key=f"{MY_API_KEY}", output_format='pandas', indexing_type='date')
    tsdata, tsmeta_data = ts.get_intraday(symbol=equity, interval='60min', outputsize='full')
    TS = tsdata.head(1000)
    path = "data/TimeSeries/"
    path += equity + ".csv"
    tsdata.to_csv(path_or_buf=path)

    ti = TechIndicators(key=f"{MY_API_KEY}", output_format='pandas', indexing_type='data')
    tidata, timeta_data = ti.get_bbands(symbol=equity, interval='60min', time_period=60)
    TI = tidata.head(1000)
    path = "data/TechIndicators/"
    path += equity + ".csv"
    tidata.to_csv(path_or_buf=path)

