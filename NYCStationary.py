"""
Name:  Ryan Chevarria
Email: Ryan.Chevarria64@myhunter.cuny.edu
Description: Visualization for NYC_Stationary data
"""

import pandas as pd
import pandasql as psql
import matplotlib.pyplot as plt
import matplotlib.style as style
import numpy as np
import re

df = pd.read_csv("NYC_Stationary.csv")
df_filter = pd.read_csv("NYC_Stationary.csv", skiprows=2)


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

q_2 = 'SELECT SUM("CY 2016") AS "CY 2016", SUM("CY 2017") AS "CY 2017", SUM("CY 2018") AS "CY 2018", SUM("CY 2019") AS "CY 2019" FROM filteredDF WHERE Category = "Residential"'
residentialSums = psql.sqldf(q_2)
residentialSums = pd.DataFrame(residentialSums)

q_3 = 'SELECT SUM("CY 2016") AS "CY 2016", SUM("CY 2017") AS "CY 2017", SUM("CY 2018") AS "CY 2018", SUM("CY 2019") AS "CY 2019" FROM filteredDF WHERE Category = "Commercial and Institutional"'
commercialSums = psql.sqldf(q_3)
commercialSums = pd.DataFrame(commercialSums)

residentialTotals = []
commercialTotals = []
for s in colNames:
    residentialTotals.append(float(residentialSums[s]))
    commercialTotals.append(float(commercialSums[s]))

newDF = pd.DataFrame({'Year' : colNames,
                      'Residential GHG' : residentialTotals,
                      'Commercial GHG' : commercialTotals
                      })
print(newDF)

x = newDF["Year"]
y = newDF["Residential GHG"]
z = newDF["Commercial GHG"]

resi = plt.plot(x, y, label = "Residential GHG", color = "purple")
comm = plt.plot(x, z, label = "Commercial GHG", color = "orange")
plt.title('Residencial and Commercial GHG Emissions', fontsize = 13, weight = 'bold', alpha = .75)
plt.ticklabel_format(style='plain', axis='y')
plt.ylabel('GHG', fontsize = 12)
plt.xlabel('Year', fontsize = 12)
plt.legend()
plt.tight_layout()
fig = plt.gcf()
fig.savefig('ResidentialandCommercialEmissions.png')


#Total of both residential and commercial emissions
q_4 = 'SELECT "CY 2016", "CY 2017", "CY 2018", "CY 2019" FROM filteredDF WHERE Category = "TOTALS"'
total = psql.sqldf(q_4)
total = pd.DataFrame(total)


totalArr = []
for g in colNames:
    totalArr.append(float(total[g]))
    

total = pd.DataFrame({'Year' : colNames,
                      'Stationary GHG' : totalArr
                      })
print(total)

style.use('fivethirtyeight')
total.plot(x = "Year", y = "Stationary GHG", lw = 2.5)
plt.ylabel('Stationary GHG', fontsize = 12)
plt.xlabel('Year', fontsize = 12)
plt.ticklabel_format(style='plain', axis='y')
plt.title('Stationary Greenhouse Gases Emissions', fontsize = 13, weight = 'bold', alpha = .75)
plt.tight_layout()

fig = plt.gcf()
fig.savefig("Stationary.png")



