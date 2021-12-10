"""
Name:  Ryan Chevarria
Email: Ryan.Chevarria64@myhunter.cuny.edu
Description: Visualization for NYGasPrices data
"""

import pandas as pd
import pandasql as psql
import matplotlib.pyplot as plt
import matplotlib.style as style
import numpy as np
import re

df = pd.read_csv("NY_GasPrices.csv", skiprows=2)
df = df.iloc[:-1, :]    #Last empty row is dropped

#Creating Year Column
year = []
for i in df['Date']:
    year.append(int(i[4:8]))

df['Year'] = year

#df_new will only contain the Year column and Gas prices, from 2016 to present
q = 'SELECT Year, "New York City Regular All Formulations Retail Gasoline Prices (Dollars per Gallon)" AS  GasPrices FROM df WHERE Year >= 2016'
gas = psql.sqldf(q)
df_new = pd.DataFrame(gas)

#df_new will now be grouped by the year and the average price is computed for each year
q_2 = 'SELECT Year, AVG(GasPrices) as AvgGasPrices FROM df_new GROUP BY Year'
avgGas = psql.sqldf(q_2)
df_new = pd.DataFrame(avgGas)

print(df_new)

style.use('fivethirtyeight')

df_new = df_new.plot(x = "Year", y = "AvgGasPrices", lw = 3)
plt.ylabel('Gas Prices', fontsize = 12)
plt.xlabel('Year', fontsize = 12)
plt.title('Average Gas Prices 2016-2021', fontsize = 13, weight = 'bold', alpha = .75)
plt.tight_layout()

fig = plt.gcf()
fig.savefig("gasPrices.png")
plt.show()


