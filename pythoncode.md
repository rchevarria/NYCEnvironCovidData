## Python Programs

[Main Project Page](https://rchevarria.github.io/NYCEnvironCovidData/)


```
f_gas = pd.read_csv("NY_GasPrices.csv", skiprows=2)
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

```


### Markdown


Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [Basic writing and formatting syntax](https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/rchevarria/NYCEnvironCovidData/settings/pages). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://support.github.com/contact) and we’ll help you sort it out.
