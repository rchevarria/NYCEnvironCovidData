"""
Name:  Ryan Chevarria
Email: Ryan.Chevarria64@myhunter.cuny.edu
Description: Visualization for NYC_Transportation data
"""

import pandas as pd
import pandasql as psql
import matplotlib.pyplot as plt
import matplotlib.style as style
import numpy as np
import re

df = pd.read_csv("NYC_Transportation.csv")
df_filter = pd.read_csv("NYC_Transportation.csv", skiprows=2)


pattern = r'CY +[0-9]{4}'
colNames = []

for i in df:
    if(re.match(pattern, str(i))):
       colNames.append(i)

q = 'SELECT "CY 2016", "CY 2017", "CY 2018", "CY 2019" FROM df WHERE "CY 2016" not like "%[^0-9]%" and "CY 2016" != "tCO2e"'
numeric = psql.sqldf(q)


numericCols = pd.DataFrame(numeric)


filteredDF = pd.DataFrame({
    "Category" : df_filter["(Category, Label)"],
    "CY 2016" : numericCols["CY 2016"],
    "CY 2017" : numericCols["CY 2017"],
    "CY 2018" : numericCols["CY 2018"],
    "CY 2019" : numericCols["CY 2019"],
    })

#The data has been scraped now it is ready to be processed

q_2 = 'SELECT SUM("CY 2016") AS "CY 2016", SUM("CY 2017") AS "CY 2017", SUM("CY 2018") AS "CY 2018", SUM("CY 2019") AS "CY 2019" FROM filteredDF WHERE Category = "On-Road"'
roadSums = psql.sqldf(q_2)
roadSums = pd.DataFrame(roadSums)

q_3 = 'SELECT SUM("CY 2016") AS "CY 2016", SUM("CY 2017") AS "CY 2017", SUM("CY 2018") AS "CY 2018", SUM("CY 2019") AS "CY 2019" FROM filteredDF WHERE Category = "Railways"'
trainSums = psql.sqldf(q_3)
trainSums = pd.DataFrame(trainSums)

roadTotals = []
trainTotals = []
for t in colNames:
    roadTotals.append(float(roadSums[t]))
    trainTotals.append(float(trainSums[t]))

newDF = pd.DataFrame({'Year' : colNames,
                      'Road GHG' : roadTotals,
                      'Train GHG' : trainTotals
                      })
print(newDF)

fig,ax = plt.subplots()
ax.plot(newDF['Year'], newDF['Road GHG'], color = "red")
plt.ticklabel_format(style='plain', axis='y')
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Road GHG", color = "red", fontsize = 12)

#twin object for two different y axis
ax2 = ax.twinx()
ax2.plot(newDF['Year'], newDF['Train GHG'], color = "blue")
ax2.set_ylabel("Train GHG", color = "blue", fontsize=12)
plt.title('Road and Train Greenhouse Gases Emissions', fontsize = 13, weight = 'bold', alpha = .75)
plt.ticklabel_format(style='plain', axis='y')
plt.tight_layout()

fig.savefig('RoadandTrainEmissions.png',
            format='png',
            dpi=100,
            bbox_inches='tight')


#Total of both road travel and train travel
q_4 = 'SELECT "CY 2016", "CY 2017", "CY 2018", "CY 2019" FROM filteredDF WHERE Category = "TOTALS"'
total = psql.sqldf(q_4)
total = pd.DataFrame(total)


totalArr = []
for g in colNames:
    totalArr.append(float(total[g]))
    

total = pd.DataFrame({'Year' : colNames,
                      'Transportation GHG' : totalArr
                      })
print(total)

style.use('fivethirtyeight')

total = total.plot(x = "Year", y = "Transportation GHG", lw = 2.5)
plt.ylabel('Transportation GHG', fontsize = 12)
plt.xlabel('Year', fontsize = 12)
plt.ticklabel_format(style='plain', axis='y')
plt.title('Transportation Greenhouse Gases Emissions', fontsize = 13, weight = 'bold', alpha = .75)
plt.tight_layout()

fig = plt.gcf()
fig.savefig("Transportation.png")



