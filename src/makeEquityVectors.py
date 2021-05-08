"""
this module extract equity data and convert to vectors. We focus only on the changes of price points.
"""
import csv
import numpy as np


def getEquityData(path):
    data = None
    with open(path, newline='') as csvfile:
        data = list(csv.reader(csvfile))
    return data


# get vector data from csv
mycsvpath = 'data/TimeSeries/AAPL.csv'
raw = getEquityData(mycsvpath)

vectors = list()
for entry in raw:
    vectors.append(entry[1:-1])


# flip the table to start from the oldest date and end with the latest entry
vectors = list(reversed(vectors[1:-1]))


"""
next we need to normalize the vectors:
"""
# convert to numpy array for ease of processing
vectors = np.array(vectors, dtype='float')
v_end   = vectors[-1]
v_start = vectors[0]

normed  = (vectors - v_start)/abs(v_start - v_end)


"""
the we run the perceptron from start to end, and compare the output with the end vector.
"""
