"""
Name:  Ryan Chevarria
Email: Ryan.Chevarria64@myhunter.cuny.edu
Description: After uniting our all dataframes and keeping data from 2016-2019, we find the
correlation between Gas prices and the rest of the pieces of data and the
correlation between Expenditure and the rest of the pieces of data. 
"""
import pandas as pd
import pandasql as psql
import matplotlib.pyplot as plt
import numpy as np
import re


#------------------GAS------------------------------------------------------
df_gas = pd.read_csv("NY_GasPrices.csv", skiprows=2)
df_gas = df_gas.iloc[:-1, :]    #Last empty row is dropped

#Creating Year Column
gas_year = []
for i in df_gas['Date']:
    gas_year.append(int(i[4:8]))

df_gas['Year'] = gas_year

#df_new will only contain the Year column and Gas prices, from 2016 to present
q_gas_1 = 'SELECT Year, "New York City Regular All Formulations Retail Gasoline Prices (Dollars per Gallon)" AS  GasPrices FROM df_gas WHERE Year >= 2016 and Year <= 2019'
gas = psql.sqldf(q_gas_1)
dfGas_Result = pd.DataFrame(gas)

#df_new will now be grouped by the year and the average price is computed for each year
q_2 = 'SELECT Year, AVG(GasPrices) as AvgGasPrices FROM dfGas_Result GROUP BY Year'
avgGas = psql.sqldf(q_2)
dfGas_Result = pd.DataFrame(avgGas)

#print(dfGas_Result)


#------------------Waste------------------------------------------------------
df_waste = pd.read_csv("NYC_Waste.csv")

pattern = r'CY +[0-9]{4}'
wasteNames = []

for i in df_waste:
    if(re.match(pattern, str(i))):
       wasteNames.append(i)

waste_totals = []
for j in wasteNames:
    waste_totals.append(float(df_waste[j].iloc[-1]))


dfWaste_Result = pd.DataFrame({'Year' : wasteNames,
                      'Waste GHG' : waste_totals
                    })
#print(dfWaste_Result)


#------------------Transportation------------------------------------------------------
df_transportation = pd.read_csv("NYC_Transportation.csv")
df_transportation_filter = pd.read_csv("NYC_Transportation.csv", skiprows=2)


pattern = r'CY +[0-9]{4}'
transportationNames = []

for i in df_transportation:
    if(re.match(pattern, str(i))):
       transportationNames.append(i)

q = 'SELECT "CY 2016", "CY 2017", "CY 2018", "CY 2019" FROM df_transportation WHERE "CY 2016" not like "%[^0-9]%" and "CY 2016" != "tCO2e"'
transportation_numeric = psql.sqldf(q)


transportation_numericCols = pd.DataFrame(transportation_numeric)


filtered_transportationDF = pd.DataFrame({
    "Category" : df_transportation_filter["(Category, Label)"],
    "CY 2016" : transportation_numericCols["CY 2016"],
    "CY 2017" : transportation_numericCols["CY 2017"],
    "CY 2018" : transportation_numericCols["CY 2018"],
    "CY 2019" : transportation_numericCols["CY 2019"],
    })

q_transportation = 'SELECT "CY 2016", "CY 2017", "CY 2018", "CY 2019" FROM filtered_transportationDF WHERE Category = "TOTALS"'
dfTransportation_Result = psql.sqldf(q_transportation)
dfTransportation_Result = pd.DataFrame(dfTransportation_Result)


transportation_totalArr = []
for g in transportationNames:
    transportation_totalArr.append(float(dfTransportation_Result[g]))
    

dfTransportation_Result = pd.DataFrame({'Year' : transportationNames,
                      'Transportation GHG' : transportation_totalArr
                      })
#print(dfTransportation_Result)


#------------------Stationary------------------------------------------------------
df_stationary = pd.read_csv("NYC_Stationary.csv")
df_stationary_filter = pd.read_csv("NYC_Stationary.csv", skiprows=2)


pattern = r'CY +[0-9]{4}'
stationaryNames = []

for i in df_stationary:
    if(re.match(pattern, str(i))):
       stationaryNames.append(i)

q = 'SELECT "CY 2016", "CY 2017", "CY 2018", "CY 2019" FROM df_stationary WHERE "CY 2016" not like "%[^0-9]%" and "CY 2016" != "tCO2e"'
stationary_numeric = psql.sqldf(q)


stationary_numericCols = pd.DataFrame(stationary_numeric)


filtered_stationaryDF = pd.DataFrame({
    "Category" : df_stationary_filter["(Category, Label)"],
    "CY 2016" : stationary_numericCols["CY 2016"],
    "CY 2017" : stationary_numericCols["CY 2017"],
    "CY 2018" : stationary_numericCols["CY 2018"],
    "CY 2019" : stationary_numericCols["CY 2019"],
    })

q_stationary = 'SELECT "CY 2016", "CY 2017", "CY 2018", "CY 2019" FROM filtered_stationaryDF WHERE Category = "TOTALS"'
dfStationary_Result = psql.sqldf(q_stationary)
dfStationary_Result = pd.DataFrame(dfStationary_Result)

stationary_totalArr = []
for g in stationaryNames:
    stationary_totalArr.append(float(dfStationary_Result[g]))
    

dfStationary_Result = pd.DataFrame({'Year' : stationaryNames,
                      'Stationary GHG' : stationary_totalArr
                      })

#print(dfStationary_Result)


#------------------Expenditures------------------------------------------------------
df_exp = pd.read_csv("expenditure_NYPCEPC.csv")

pattern = r'[0-9]{4}'
expNames = []

for i in df_exp['DATE']:
    if(re.match(pattern, str(i))):
       expNames.append(i[:4])

dfExpenditure = pd.DataFrame({
    'Year' : expNames,
    'Avg Expenditure' : df_exp['NYPCEPC']
    })

q_exp = 'SELECT Year, "Avg Expenditure" FROM dfExpenditure WHERE Year >= 2016 and Year <= 2019'
exp = psql.sqldf(q_exp)
dfExpenditure_Result = pd.DataFrame(exp)

#print(dfExpenditure_Result)

###------------------Uniting into one DataFrame------------------------------------------------------###

df_ALL = pd.DataFrame({
    'GasPrices' : dfGas_Result['AvgGasPrices'],
    'Waste' : dfWaste_Result['Waste GHG'],
    'Transportation' : dfTransportation_Result['Transportation GHG'],
    'Stationary' : dfStationary_Result['Stationary GHG'],
    'Expenditures' : dfExpenditure_Result['Avg Expenditure']
    })

colList = []
for i in df_ALL:
    colList.append(i)
###------------------Finding Correlations------------------------------------------------------###

gasCor = []
for j in colList:
        if(df_ALL['GasPrices'].astype(float).corr(df_ALL[j] != 1.0)):
            abs_temp = (df_ALL['GasPrices'].astype(float).corr(df_ALL[j]).astype(float))
            gas_pair = (j, abs_temp)
            gasCor.append(gas_pair)

expCor = []
for k in colList:
        if(df_ALL['Expenditures'].astype(float).corr(df_ALL[k] != 1.0)):
            abs_temp = (df_ALL['Expenditures'].astype(float).corr(df_ALL[k]).astype(float))
            exp_pair = (k, abs_temp)
            expCor.append(exp_pair)

print("Correlations between Gas Prices and Emissions\n")
for cors in gasCor:
    print(cors)
print("\n")
print("Correlations between Expenditures and Emissions\n")    
for cors in expCor:
    print(cors)
