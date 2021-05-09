from alpha_vantage.fundamentaldata import FundamentalData
key = 'M4JP31006H3PKZ8T'
symbol = input('Ticker : ')
period = input('Period- annual, quarterly : ')
statement = input('Statement- balance sheet, income statement, cash flow : ')
fd = FundamentalData(key,output_format = 'pandas')
if period == 'annual':
    if statement == 'balance sheet':
        state = fd.get_balance_sheet_annual(symbol)[0].T[2:]
        state.columns = list(fd.get_balance_sheet_annual(symbol)[0].T.iloc[0])
    elif statement == 'income statement':
        state = fd.get_income_statement_annual(symbol)[0].T[2:]
        state.columns = list(fd.get_income_statement_annual(symbol)[0].T.iloc[0])
    elif statement == 'cash flow':
        state = fd.get_cash_flow_annual(symbol)[0].T[2:]
        state.columns = list(fd.get_cash_flow_annual(symbol)[0].T.iloc[0])
    else:
        print("wrong input given by the user ")

elif period == 'quarterly':
    if statement == 'balance sheet':
        state = fd.get_balance_sheet_quarterly(symbol)[0].T[2:]
        state.columns = list(fd.get_balance_sheet_quarterly(symbol)[0].T.iloc[0])
    elif statement == 'income statement':
        state = fd.get_income_statement_quarterly(symbol)[0].T[2:]
        state.columns = list(fd.get_income_statement_quarterly(symbol)[0].T.iloc[0])
    elif statement == 'cash flow':
        state = fd.get_cash_flow_quarterly(symbol)[0].T[2:]
        state.columns = list(fd.get_cash_flow_quarterly(symbol)[0].T.iloc[0])
    else:
        print('Wrong Entry')
else:
    print('Wrong Entry')
print(state)