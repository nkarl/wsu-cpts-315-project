"""
From the Alpha Vantage API, we are going to use Intraday (Extended history)
for our data set. Within this set (containing over 2 million minute-points),
we will use the 60-minute-points instead to cut down on the size of our input.
"""
import time
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.sectorperformance import SectorPerformances
from pprint import pprint
from matplotlib import pyplot

# MY_API_KEY = 'M4JP31006H3PKZ8T'


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


def getData(equity, MY_API_KEY):
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


def getKeyList(keypath):
    """
    get a list of all keys to cycle through while parsing, to avoid exhausting each key.

    :param keypath (list): a list of keys available from keypath.
    """
    key_list = list()
    with open(keypath) as keyfile:
        key_list = keyfile.read().splitlines()
    return key_list


def parseAllDataToCSV(company_list, key_list):
    """
    make API calls and requests data for the given list of companies.

    :param company_list (list): list of companies to request data from
    :param key_list (list): list of keys to cycle through
    """
    j = 0  # starting from key at j position
    for i in range(len(company_list)):
        # if len(key_list) < 5:
            # time.sleep(30 / len(key_list))  # sleep for some time before making the next API call

    # resets the key list if reached last key
        print((company_list[i], key_list[j]))
        # getData(company_list[i], key_list[j])
        if j == len(key_list) - 1:
            j = 0
        else:
            j += 1
