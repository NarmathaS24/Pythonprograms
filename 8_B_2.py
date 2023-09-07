import pandas as pd
import numpy as np
from pandas.tseries.offsets import BMonthEnd
year = 2023
dates = pd.date_range(start=str(year), end=str(year+1), freq='B')
last_bdays = dates + BMonthEnd(0)
last_workdays = last_bdays[last_bdays.weekday < 5]
print(last_workdays)
