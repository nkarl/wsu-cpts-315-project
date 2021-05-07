"""This is the main module for our project.
"""
import parser
import time


# path to alpha vantage API keys
keypath = "apikey.key"
mock_keypath = "mockkeys.key"

# list of our companies to test
SP500_SYMBOLS = ['MMM', 'ABT', 'GOOGL', 'AMZN', 'MSFT']

# parse all data for the given list of companies
parser.parseAllDataToCSV(SP500_SYMBOLS, parser.getKeyList(keypath))
