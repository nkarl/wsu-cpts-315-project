"""
this module extract equity data and convert to vectors.
"""
import csv

def getEquityData(path):
    data = None
    with open(path, newline='') as csvfile:
        data = list(csv.reader(csvfile))
    return data


# test
mycsvpath = 'data/TimeSeries/AAPL.csv'

aa = getEquityData(mycsvpath)
