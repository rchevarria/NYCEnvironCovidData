"""
Name:  Ryan Chevarria
Email: Ryan.Chevarria64@myhunter.cuny.edu
Description: Visualization for NYCExpenditure data
"""

import pandas as pd
import pandasql as psql
import matplotlib.pyplot as plt
import matplotlib.style as style
import numpy as np
import re

df = pd.read_csv("expenditure_NYPCEPC.csv")

print(df)

pattern = r'[0-9]{4}'
colNames = []

for i in df['DATE']:
    if(re.match(pattern, str(i))):
       colNames.append("CY " + i[:4])

newDF = pd.DataFrame({
    'Year' : colNames,
    'Avg Expenditure' : df['NYPCEPC']
    })

style.use('fivethirtyeight')

newDF = newDF.plot(x = "Year", y = "Avg Expenditure", lw = 3)
plt.ylabel('Annual Spending', fontsize = 12)
plt.xlabel('Year', fontsize = 12)
plt.title('Per Capita Personal Consumption Expenditures', fontsize = 13, weight = 'bold', alpha = .75)
plt.tight_layout()

fig = plt.gcf()
fig.savefig("Expenditure.png")
plt.show()

