from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.sectorperformance import SectorPerformances
# from pprint import pprint

import threading
import matplotlib.pyplot as plt


MY_API_KEY = 'M4JP31006H3PKZ8T'


# PLOTTING TIME SERIES, INTRA-MINUTE VALUE FOR 'MSFT'
# Using matplotlib, graph the minute to minute changes
def timeSeries(tsdata):
    tsdata['4. close'].plot()
    plt.title('Intraday Times Series for the MSFT stock (1min)')
    plt.show()
    pass


def tiInd():
    tidata.plot()
    plt.title('BBands indicator for MSFT stock (60min)')
    plt.show()
    pass


def sPerf(spdata):
    spdata['Rank A: Real-Time Performance'].plot(kind='bar')
    plt.title('Real Time Performance (%) per Sector')
    plt.tight_layout()
    plt.grid()
    plt.show()
    pass


# ts = TimeSeries(key="{}".format(MY_API_KEY), rapidapi=True,
                    # output_format='pandas',
                    # indexing_type='date')
ts = TimeSeries(key="{}".format(MY_API_KEY), output_format='pandas',
                    indexing_type='date')
tsdata, tsmeta_data = ts.get_intraday(symbol='MSFT', interval='1min', outputsize='full')
tsp = threading.Thread(name='timeSeries', target=timeSeries)
# pprint(tsdata.head(200))

ti = TechIndicators(key="{}".format(MY_API_KEY), output_format='pandas',
                        indexing_type='data')
tidata, timeta_data = ti.get_bbands(symbol='MSFT', interval='60min',
                                        time_period=60)
# pprint(tidata.head(200))
tip = threading.Thread(name='tiInd', target=tiInd)

sp = SectorPerformances(key="{MY_API_KEY}", output_format='pandas')
spdata, spmeta_data = sp.get_sector()
spp = threading.Thread(name='SP', target=sPerf)
# pprint(spdata.head(200))

tsp.start()
tip.start()
spp.start()
