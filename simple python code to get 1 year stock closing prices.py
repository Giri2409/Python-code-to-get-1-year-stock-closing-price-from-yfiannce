# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 11:44:15 2023

@author: bopg001
"""

!pip install yfinance

import yfinance as yf
from datetime import datetime, time

start=datetime.now()
end= start.replace(year=start.year-1)

data=yf.download("TSLA",end,start)

close=data["Close"]
ax=close.plot(title="TESLA")
ax.set_xlabel("Date")
ax.set_ylabel("Closing price")
ax.grid()

