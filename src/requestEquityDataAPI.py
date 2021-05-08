"""
From the Alpha Vantage API, we are going to use Intraday (Extended history)
for our data set. Within this set (containing over 2 million minute-points),
we will use the 60-minute-points instead to cut down on the size of our input.

Because there is a limit to how many API calls a standard account can make per
day, we were limited to a small data set of only a few companies in the list of
S&P 500 companies.
"""
import time
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.sectorperformance import SectorPerformances
from pprint import pprint
from matplotlib import pyplot


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
    # Pandaframe for TimeSeries
    ts = TimeSeries(key=f"{MY_API_KEY}", output_format='pandas', indexing_type='date')
    tsdata, tsmeta_data = ts.get_intraday(symbol=equity, interval='60min', outputsize='full')
    TS = tsdata.head(1000)
    path = "data/TimeSeries/"
    path += equity + ".csv"
    tsdata.to_csv(path_or_buf=path)

    # Pandaframe for TechIndicators
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


def requestEquityData(company_list, key_list, DBUG=False):
    """
    make API calls and requests data for the given list of companies.

    :param company_list (list): list of companies to request data from
    :param key_list (list): list of keys to cycle through
    :param DBUG (Bool): for debuggin purpose; only make API calls when False
    """
    j = 0  # starting from key at j position
    for i in range(len(company_list)):
        # given a limited list of keys, we need to avoid exhausting the API call quota
        if len(key_list) < 5:  
            time.sleep(15 / len(key_list))  # sleep for some time before making the next API call

        # couple each symbol with a key, and make the API call
        print((company_list[i], key_list[j]))
        if not DBUG:
            getData(company_list[i], key_list[j])

        # resets the key list if reached last key
        j = 0 if (j == len(key_list) - 1) else j + 1
