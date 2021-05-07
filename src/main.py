"""This is the main module for our project.
"""
import parser


# test
SP500_SYMBOLS = ['MMM', 'ABT', 'GOOGL', 'AMZN', 'MSFT']

for symbol in SP500_SYMBOLS:
    parser.getData(symbol)
