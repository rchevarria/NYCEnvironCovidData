## New York City's Environmental Footprint and COVID-19

### Introduction

People’s lives were disrupted by COVID-19, millions remained home for an
extended amount of time. This resulted in a pause of daily commutes, outdoor/indoor activities, 
reduced incomes, and consumerism. I want to use data analysis to see how this situation reduced 
New Yorker’s environmental footprint, and how future return to normalcy will impact these trends.

### Brief Description

This project seeks to view connections between NYC's inactivity/shutdown during the pandemic and 
its effect on the environment. To establish these connections I am using data bases pertaining to 
gas prices, stationary emissions, transportation emissions, waste emissions and per capita 
expenditures. Through the use of pandas, SQL, regex, matplotlib, and other python methods, I am 
able to portray these pieces of data in a meaningful way, in which they show connections to each 
other. 

### Relevance to NYC

This connects to NYC as it is a very dense city that was largely inactive due to the pandemic 
and the consequent shutdowns. As a big crowded city, New York's environmental footprint is large, 
therefore this period of time of closure likely had an effect. The data used in this project 
pertain's to NYC and seeks to highlight New Yorker's overall activity before and after the 
pandemic as well as the city's emission trends. 

### Visuals

**The following visuals show New Yorker's activity from 2016-2021 
in regards to average yearly gas prices and per capita expenditure**


<img src="https://raw.githubusercontent.com/rchevarria/NYCEnvironCovidData/gh-pages/gasPrices.png" width="420" height="340"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <img src="https://raw.githubusercontent.com/rchevarria/NYCEnvironCovidData/gh-pages/Expenditure.png" width="420" height="340">  




**The following visuals show NYC's Emission Data 
in regards to Transportation, Stationary, Waste emissions
measured in GHG**


<img src="https://raw.githubusercontent.com/rchevarria/NYCEnvironCovidData/gh-pages/Transportation.png" width="370" height="290"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <img src="https://raw.githubusercontent.com/rchevarria/NYCEnvironCovidData/gh-pages/RoadandTrainEmissions.png" width="350" height="270">  


<img src="https://raw.githubusercontent.com/rchevarria/NYCEnvironCovidData/gh-pages/Stationary.png" width="370" height="290"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <img src="https://raw.githubusercontent.com/rchevarria/NYCEnvironCovidData/gh-pages/ResidentialandCommercialEmissions.png" width="350" height="270">  


<img src="https://raw.githubusercontent.com/rchevarria/NYCEnvironCovidData/gh-pages/Waste.png" width="370" height="290"> 

Some notes on the visuals above:
- Average Gas Prices is shown from 2016-2021. It is the average yearly gas price in NYC. 
- Per Capita Personal Consumption Expenditures is the value of the goods and services purchased by New York residents.
- Transportation GHG shows the total tCO2e or GHG of vehicle/road and train transportation emitted by NYC 2016-2019
  - Road and Train GHG separates the two modes of travel, as road travel far exceeds emissions of train travel
  - Road travel includes: buses, heavy/medium trucks, passenger cars, and SWCV.
  - Train travel includes: railway consumption of diesel and electricity 
- Stationary GHG shows the total tCO2e or GHG emitted by residencies and commercial businesses in NYC 2016-2019
  - Residential and Commercial GHG separates the two structures, as residential emissions exceed commercial emissions.
  - Residential GHG's include: different fuel oils, biofuel, electricity, natural gas and steam
  - Commercial GHG's include: different fuel oils, biofuel, electricity, natural gas and steam   
- Waste GHG shows the total tCO2e or GHG emitted by landfills 




### Correlations

### Analysis

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
