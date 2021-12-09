## Datasets and Techniques

[Main Project Page](https://rchevarria.github.io/NYCEnvironCovidData/)

<img src="https://raw.githubusercontent.com/rchevarria/NYCEnvironCovidData/gh-pages/Data1.jpg" width="300" height="186" align="center" background-color:transparent> 

### Data

The data for this project derives from 3 different open source databases that provide us with the 5 different data sets used. These include the "New York City Regular All Formulations Retail Gasoline Prices" from the [eia U.S. Energy Information Administration](https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=pet&s=emm_epmr_pte_y35ny_dpg&f=m), the "Per Capita Personal Consumption Expenditures: Total for New York (NYPCEPC) from the [Economic Research Federal Reserve Bank of St. Louis](https://fred.stlouisfed.org/series/NYPCEPC), and the "Inventory of New York City Greenhouse Gas Emissions" from the [NYC Mayor's Office of Sustainability](https://nyc-ghg-inventory.cusp.nyu.edu). 

The NYC gas dataset provided by the eia, provides New York City's Regular all formulations retail gasoline prices in dollars per gallon. The dataset downloaded contains the price per gallon of every month from the year 2000 up to October 2021. The Per Capita Personal Consumption Expenditures dataset provides annual personal consumption expenditures of a given area divided by the resident population of the area, in this case the area being New York and the years provided from 1997 to 2020. The NYC GHG inventory provides us with the Citywide Inventory and City Government Inventory of GHG information. For this project I utilized the Citywide Inventory which consists of direct and indirect GHG emissions from- Stationary energy: energy used by buildings and other stationary sources, as well as fugitive emissions from natural gas distribution; Transportation: on-road transportation, railways, marine navigation, and aviation; and Waste: wastewater treatment, and solid waste generated - all within the city's boundaries. This inventory that provides us with these 3 datasets, contains emission data from the years 2005 to 2019 and with two metric units - GHG (tCO₂e) and Source Energy (MMBtu), for this project I used GHG. 

### Techniques

In order to narrow the data to be able to find connections between our activity data (gas & expenditures) and our GHG emissions data (stationary, transportation, & waste) I decided to maintain our datasets within the years 2016 and 2019. To maintain a uniformly (x = year and y = dependent piece of data) structure for the visuals and later correlation findings, I utilized pandas, SQL, regex, matplotlib along with other python methods to reduce the number of columns/rows that contained irrelevant or useless information. 

***NYC Gas Prices:***
In the case of NYC gas prices dataset I created a new dataframe that stores the year and the corresponding year's average gas price. To do this SQL was used to format and filter the desired years, and the 12 months were grouped by year to compute the average. (for example, in 2016 the average gas price was $2.13)

***NYC Per Capita Personal Expenditures:***
For NYC expenditure (NYPCEPC dataset I created a new dataframe that formats and stores the year and the corresponding year's average citizen expenditure.(for example in 2016 the average citizen spent $45202) 

***NYC Waste Emissions:***
For NYC Waste emissions dataset I created a new dataframe that formats and stores the year and the corresponding year's emissions produced by waste or more specifically solid waste/landfills. To do this, regex was used to filter out the years from the dataset among removing empty spaces and labels that would have conflicted in creating our visuals. (for example in 2016 the total waste GHG emissions was 1893833.414 GHG (tCO₂e))

***NYC Transportation Emissions:***
For NYC Transportation emissions dataset I created a new dataframe that formats and stores the year and the corresponding year's emissions produced by modes of transportation, more specifically I narrowed down categories to "on-road" which includes buses, heavy duty trucks, medium duty trucks, passenger cars and SWCV; and "railways" which includes the diesel and electricity used by trains. To do this, SQL was used to filter out the years and the desired categories. For this dataset two visuals were created, one that showed the totals for road and train emissions separately, and another one that showed total emissions produced by both modes of transportation. This was done to highlight road transportation far outweighing the amount of emissions produced by train transportation. (for example in 2016, road transportation produced around 14,910,000 GHG(tCO₂e), train transportation produced around 696,706 GHG(tCO₂e), and both combined produced close to 15,540,000 GHG(tCO₂e))

***NYC Stationary Emissions:***
For NYC Stationary emissions dataset I created a new dataframe that formats and stores the year and the corresponding year's emissions produced by sectors, more specifically I narrowed down categories to "Residential" and "Commercial and Institutional". These include emission sources related to #2 fuel oil, #4 fuel oil, #6 fuel oil, Biofuel, electricity, natural gas and steam. To do this, SQL was used to filter out the years and the desired categories. For this dataset two visuals were created, one that showed the totals for residential and commercial emissions separately, and another one that showed total emissions produced by both. This was done to highlight residential emissions far outweigh those of commercial. (for example in 2016, residential emissions produced around 17,764,690 GHG(tCO₂e), commercial emissions produced around 14,674,320 GHG(tCO₂e), and both combined produced close to 37,000,000 GHG(tCO₂e)).

