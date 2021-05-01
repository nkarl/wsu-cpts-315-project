from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.sectorperformance import SectorPerformances
from pprint import pprint

from matplotlib import pyplot


MY_API_KEY = 'M4JP31006H3PKZ8T'


# PLOTTING TIME SERIES, INTRA-MINUTE VALUE FOR 'MSFT'
# Using matplotlib, graph the minute to minute changes
ts = TimeSeries(key="{}".format(MY_API_KEY), rapidapi=True,
                    output_format='pandas',
                    indexing_type='date')
ts = TimeSeries(key="{}".format(MY_API_KEY), output_format='pandas',
                    indexing_type='date')

tsdata, tsmeta_data = ts.get_intraday(
    symbol='MSFT', interval='1min', outputsize='full')
pprint(tsdata.head(200))
tsdata['4. close'].plot()
pyplot.title('Intraday Times Series for the MSFT stock (1min)')
# pyplot.show()


ti = TechIndicators(key="{}".format(MY_API_KEY), output_format='pandas',
                        indexing_type='data')
tidata, timeta_data = ti.get_bbands(symbol='MSFT', interval='60min',
                                    time_period=60)
pprint(tidata.head(200))
tidata.plot()
pyplot.title('BBands indicator for MSFT stock (60min)')
# pyplot.show()


sp = SectorPerformances(key="{MY_API_KEY}", output_format='pandas')
spdata, spmeta_data = sp.get_sector()
pprint(spdata.head(200))
spdata['Rank A: Real-Time Performance'].plot(kind='bar')
pyplot.title('Real Time Performance (%) per Sector')
pyplot.tight_layout()
pyplot.grid()
# pyplot.show()
