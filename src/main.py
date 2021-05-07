"""This is the main module for our project.
"""
import parser
import time


# test
SP500_SYMBOLS = ['MMM', 'ABT', 'GOOGL', 'AMZN', 'MSFT']

for symbol in SP500_SYMBOLS:
    time.sleep(60)  # sleep for 1 minute before the next API call
    parser.getData(symbol)
