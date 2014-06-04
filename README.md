##Project Description

Build a platform where the user can upload a dataset and the algorithm would return the most highly correlated open datasets and allow the user to further explore these correlations.

The goal of the platform would be to offer the ability to choose the best algorithms to find similarity or causation depending on her use case and give her access to every open datasets without having to manually search for them and load them. 

Tag Line:  A discovery tool for open time series data based on correlations.
Use Cases: Finance, Macroeconomic data, Education, Environment, Health, ...


##Current Development State
A first proof of concept was developed during Montreal's Big Data Week. It connects to the Quandl API, loads 20 data sets and rank them depending on their correlation (Pearson's r) to the reference dataset. Then it visualize the most correlated.

##Road Map
- [ ] Automatically load datasets using the quandl API
- [ ] Implement several algorithms to compare datasets
- [ ] Visualize top10 most correlated datasets
- [ ] Navigate through datasets to better understand the correlations

###Longer term
Human input: give the ability to the user to mention that a correlation is meaningful and not just random.
Forecast: Embed time series prediction based on known causations
Adapt the platform to various use cases.
