"""
From the Alpha Vantage API, we are going to use Intraday (Extended history)
for our data set. Within this set (containing over 2 million minute-points),
we will use the 60-minute-points instead to cut down on the size of our input.
"""

# getting the slice/snapshot of monthly data over 2 years
#-----------------------------------------------------------------------------
# each snapshot is 30-day.
slices = []
for y in range(1, 3):
    year = ""
    year += "year" + str(y)
    for i in range(1,13):
        month = ""
        month += year + "month" + str(i)
        slices.append(month)

SP500 = ['MMM', 'ABT', 'GOOGL', 'AMZN', 'MSFT']
