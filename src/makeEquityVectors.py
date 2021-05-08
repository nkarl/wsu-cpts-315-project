"""
this module extract equity data and convert to vectors. We focus only on the changes of price points.
"""
import csv
import numpy as np


def getEquityData(path):
    """
    extracts data from source csv.

    :param path [string]: path to source csv
    """
    data = None
    with open(path, newline='') as csvfile:
        data = list(csv.reader(csvfile))
    return data


def convert2Vectors(raw: list):
    """
    this function converts a raw list of lists to a numpy array of vectors

    :param raw [list]: the raw input
    """
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

    return normed, v_start, v_end


"""
then we run the perceptron from start to end, and compare the output with the end vector.
"""
# get vector data from csv
# csv_path = 'data/TimeSeries/AAPL.csv'
# raw = getEquityData(csv_path)
# x, s, e = convert2Vectors(raw)
