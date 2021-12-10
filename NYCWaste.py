"""
Name:  Ryan Chevarria
Email: Ryan.Chevarria64@myhunter.cuny.edu
Description: Visualization for NYC_Waste data
"""

import pandas as pd
import pandasql as psql
import matplotlib.pyplot as plt
import matplotlib.style as style
import numpy as np
import re


df = pd.read_csv("NYC_Waste.csv")

pattern = r'CY +[0-9]{4}'
colNames = []

for i in df:
    if(re.match(pattern, str(i))):
       colNames.append(i)

totals = []
for j in colNames:
    totals.append(float(df[j].iloc[-1]))


newDF = pd.DataFrame({'Year' : colNames,
                      'Waste GHG' : totals
                    })
print(newDF)

style.use('fivethirtyeight')

newDF = newDF.plot(x = "Year", y = "Waste GHG", lw = 2.5)
plt.ylabel('Waste GHG', fontsize = 12)
plt.xlabel('Year', fontsize = 12)
plt.title('Waste Greenhouse Gases Emissions', fontsize = 13, weight = 'bold', alpha = .75)
plt.tight_layout()

fig = plt.gcf()
fig.savefig("Waste.png")
plt.show()
