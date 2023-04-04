pg. 1
 R.V. COLLEGE OF ENGINEERING,
 BENGALURU-560059
 (Autonomous Institution Affiliated to VTU, Belagavi)

VISUALISATION AND COMPARISON OF
NIFTY50
STOCK DATASETS

 Exploratory Data Analysis Of Datasets
Python PLC Theory EL Report
Submitted By :-
SNEHIL VUKKUSILA --- RVCE22BAI006
PARTH SHUKLA---RVCE22BAI031
Department of Artifial Intelligence And Machine Learning,
 RV COLLEGE OF ENGINEERING®, BENGALURU – 560059
pg. 2
Outline

•Introduction
•Problem Statement

•Objectives
•Methodology
•Results
•Conclusion
pg. 3
Introduction and Summary
Problem Statement
The Tata Group is one of the largest conglomerates in India with businesses
ranging from steel, automobiles, and IT services to hotels, airlines, and
consumer goods. Through analysis our task is performing an exploratory data
analysis (EDA) on the stock prices of Tata Group companies over the last 10
years. We want to see how the stocks of a particular sector within a huge
conglomerate as Tata, have grown along with the group as a whole, and the
individual stock performances over a long period of growth. The goal of this
project is to identify trends and patterns in the stock prices and the range of
volatility of different Tata Group companies, and to provide insights that can
help inform investment decisions, through visualisation and comparison of
Volume, Price, Moving Averages, Market Capitalization.
We will be utilizing past data of stocks present in the Nifty 50 Index, and by
visualization and comparison we will be able to determine the risk , and
future prospects for investment into those stock
Overview
The objective of this Exploratory Data Analysis is to apply a complete datadriven analytic approach to understand the trend in the price of a stock, and
create comparisons with other stocks in same sector or group of companies.
It involves data collection, data wrangling, EDA with data visualization,
Building a Dashboard with Plotly and matplotlib, Seaborn.
Utilising Data analysis libraries and modules such as NumPy , Pandas
Scikitlearn . Visualization libraries and modules like matplotlib , Seaborn
pg. 4
Understanding the Problem Statement
Broadly, stock market analysis is divided into two parts – Fundamental Analysis and
Technical Analysis.
● Fundamental Analysis involves analyzing the company’s future profitability on the
basis of its current business environment and financial performance.
● Technical Analysis, on the other hand, includes reading the charts and using
statistical figures to identify the trends in the stock market.
To understand the risk associated with it there must be a proper analysis of
stock before buying it.
Objectives to find answers:
1)Utilising previous data predict of price, volume, volatility, market
capitalization, we will try to analyse the patterns and the similarities of the stock price
movement over a period of 15 years worth of data.
2)We will visualize the various parameters that influence stock analysis, which will
affect the decision of an investor.
3)Plot and show how stocks have different volatility values and ROI , and why some
stocks a more risky and some are consolidated in nature.
4)Analyse the moving averages of 50 day and 200 day price values, and plot these with
respect to the daily values, and see how we can predict the future movements.
pg. 5
Methodology
•Data collection methodology:
•The data was collected by sending get request to Kaggle API and by web
scraping NSE INDIA and Nifty 50 data sets Records.
•Perform data wrangling on the csv files which have been generated.
•Dealing with missing values, creating new columns, dropping irrelevant
columns and visualizing through Panda's data frames
•Perform exploratory data analysis (EDA) using Pandas and Numpy
•Perform visual analytics Plotly , Matplotlib
•Perform comparative analysis using plots and graphs
Including, Price Analysis, Volume Comparison, 50-day and 200-day Moving
Average comparison, Volatility Histogram
•Comparison analysis
pg. 6
Data Collection
How was the data collected?
•The data is collected from the Kaggle dataset, and the API will give us data
in form of a zipped file containing csv files of various stock data.
•We also use NSEIndia website to extract csv files.
•We extract the data set into the form of rows and columns which can be
easily operated upon, by using pandas, which can easily access and parse
through CSV files.
Data Wrangling

pg. 7
Data description:
•Open: The price of the stock when the market opens in the
morning.
•Close: The price of the stock when the market closed in the
evening.
•High: Highest price the stock reached during that day.
•Low: Lowest price the stock is traded on that day.
•Volume: The total amount of stocks traded on that day.
What is Stock Market Analysis?
Stock market analysis enables investors to identify the intrinsic worth of a
security even before investing in it. All stock market tips are formulated after
thorough research by experts. Stock analysts try to find out activity of an
instrument/sector/market in future. By using stock analysis, investors and
traders arrive at equity buying and selling decisions. Studying and evaluating
past and current data helps investors and traders to gain an edge in the
markets to make informed decisions. Fundamental Research and Technical
Research are two types of research used to first analyse and then value a
security.
pg. 8
Comparison of Price
According to the graph above, the price of TCS has skyrocketed
significantly higher than that of Tata Steel and Tata Motors. TCS’s
pricing trajectory has been generally upward from its beginning,
whereas Tata Steel and Tata Motors have been more on a
consolidation trend, this shows the innovative IT industry as a
whole has developed vastly, as compared to a legacy generalised
industreis such as steel ore and motor vehicles are more slow
growth, but stable and guaranteed to be used for many generations.
pg. 9
Comparison of Volume
Though the price of TCS has risen more significantly as compared
to Tata Steel and Tata Motors, we can notice from the above graph
that TCS has the least volume signifying that the stock has been
traded comparatively less as compared to Tata Steel and Tata
Motors and is lesser liquid.
Tata Motors on the other hand has been traded the most signifying
higher liquidity, and better order execution.
We can see that traders and investors who may be of a retail or FII
level investment firms, have more confidence on a stable industry
such as Tata Steel and Tata Motors and are wary about the IT industry
as it is still growing at such a rapid pace without a proven track record.
pg. 10
Moving Averages
The above shows the price, along with the 50 day and 200 day
moving average plots. As we know the stock prices are highly
volatile and prices change quickly with time. To observe any trend or
pattern we can take the help of a
50-day 200-day average
pg. 11
Volatility Analysis
It is clear from the graph that the percentage increase in stock price
histogram for TCS is the widest which indicates the stock of TCS is
the most volatile among the three companies compared.
The width of the histogram shape is related to the standard deviation of the
distribution. The higher it is the more variants we have, the variants of a
certain distribution are directly related to the standard deviation. It’s
actually the square value of the standard deviation, the higher the standard
deviation is, the higher the variance is. The more volatility we have in terms
of stock analysis.
pg. 12
Data Collection and Wrangling
pg. 13
pg. 14
Data Collection and Wrangling
Once downloaded, extract the zip file.
This data set consists of a number of companies’ stock data from 2000-2021
including Adani Ports, Bajaj Finance, Wipro, Infosys, and many more. But for
this project, we will be analyzing three Tata stocks – Tata Motors, Tata Steel,
and Tata Consultancy Services (TCS).
pg. 15
The data in the data set of the csv file opened using excel consists of Date,
Symbol, Prev Close, Open, High, Low, Last, Close, VWAP, Turnover,
Trades, Deliverable Volume, and % Deliverable. We will be utilizing the Date,
Open, and Volume.

pg. 16
Data viewing
Here, we can notice the data type of “Date” is an ‘object’ in the Tata
Motors dataset, hence we need to convert it into the ‘date’ datatype
(Which we will do in the “Working on Data” section).
You will see similar results for the datatypes for Tata Steel and TCS
datasets after executing the tata_steel.info() and tcs.info() functions
respectively.
pg. 17
From the above table, we can view the first 5 rows of the Tata Motors
dataset and get a brief overview of the data present.You will see the
results of the dataset for Tata Steel and TCS by executing the
tata_steel.head() and tcs.head() functions respectively.

pg. 18
Working on Data
Converting the “Date” column dtype from object to date
Once this code is executed, if you try executing the .info() function
on any of the datasets, you will notice the datatype of the ‘Date’
column changed from ‘object’ to
‘datetime64[ns]’ for all 3 datasets
Dropping columns Trades, Deliverable Volume, and %Deliverable
Once this code is executed, if you try running the .head() or .tail()
function on any of the datasets, you will notice all the 3 columns
Trades, Deliverable Volume, and %Deliverable not present.
pg. 19
Once this code is executed, if you try running the .head() or .tail()
function on any of the datasets, you will notice 3 new columns
‘Day’, ‘Month’ and ‘Year’ present. We will be using the ‘Day’
column for our analysis

pg. 20
EDA with Data Visualization
Visualization charts and reason for the choice of the
chart
•Bar Graph makes it easy to compare sets of data between different groups
immediately. The graph represents categories on one axis and a discrete
value in the other. The goal is to show the relationship between the two
axes. Bar charts can also show big changes in data over time. Mean vs.
Orbit
•Line Graphs are useful in that they show data variables and trends very
clearly and can help to make predictions about the results of data not yet
recorded


pg. 21
Price Comparision
The next segment of code creates a plot showing the relationship
between the opening price of each company's stock over time. It plots
the 'Open' column against the 'Date' column for each company, sets
the title and axes labels, and adds a legend for clarity.

pg. 22
Volume Comparision
The next plot shows the relationship between the volume of each
company's stock over time. It plots the 'Volume' column against the
'Date' column for each company, sets the title and axes labels, and
adds a legend for clarity.

pg. 23
Moving Averages
The following segment of code creates a plot showing the rolling
average of TCS's opening stock price over time. It calculates the
rolling average using the 'rolling' function and plots the 'Open',
'MA50', and 'MA200' columns against the 'Date' column, sets the
title, and adds a legend and gridlines for clarity.

pg. 24
Volatility Analysis
The final segment of code creates a histogram showing the
distribution of returns for each company's stock. It calculates the
daily returns for each company by dividing the 'Close' column by the
previous day's 'Close' value and subtracting 1. It then creates a
histogram with 100 bins for each company's returns, sets the title,
adds a legend, and displays the plot.
pg. 25





Code







import pandas as pd
import matplotlib.pyplot as plt
tata_motors=pd.read_csv("C:/Users/svukk/PycharmProjects/TheoryEL/TA
TAMOTORS.csv")
tata_steel=pd.read_csv("C:/Users/svukk/PycharmProjects/TheoryEL/TAT ASTEEL.csv")
tcs=pd.read_csv("C:/Users/svukk/PycharmProjects/TheoryEL/TCS.csv")
tata_motors["Date"]=pd.to_datetime(tata_motors["Date"])
tata_steel["Date"]=pd.to_datetime(tata_steel["Date"])
tcs["Date"]=pd.to_datetime(tcs["Date"])
tata_motors=tata_motors.drop(['Trades','Deliverable Volume','%Deliverble'], axis=1)
tata_steel=tata_steel.drop(['Trades','Deliverable Volume','%Deliverble'], axis=1)
tcs=tcs.drop(['Trades','Deliverable Volume','%Deliverble'], axis=1)
tata_motors['Month']=tata_motors["Date"].dt.month
tata_motors['Year']=tata_motors["Date"].dt.year
tata_motors['Day']=tata_motors["Date"].dt.day
tata_steel['Month']=tata_steel["Date"].dt.month tata_steel['Year']=tata_steel["Date"].dt.year
pg. 26
tata_steel['Day']=tata_steel["Date"].dt.day
tcs['Day']=tcs['Date'].dt.day tcs['Year']=tcs['Date'].dt.year
tcs['Month']=tcs['Date'].dt.month
plt.figure(figsize=(20,7))
plt.plot(tata_motors['Date'],tata_motors['Open'],color='blue',label='Tata Motors')
plt.plot(tata_steel['Date'],tata_steel['Open'],color='grey',label='Tata Steel')
plt.plot(tcs['Date'],tcs['Open'],color='orange',label='TCS') plt.title("Relation
between Tata Motors, Tata Steel and TCS Price") plt.xlabel("Year")
plt.ylabel("Price") plt.legend(title="")
#plt.show()
plt.figure(figsize=(20,7))
plt.plot(tata_motors['Date'],tata_motors['Volume'],color='blue',label='Tata Motors')
plt.plot(tata_steel['Date'],tata_steel['Volume'],color='grey',label='Tata Steel')
plt.plot(tcs['Date'],tcs['Volume'],color='orange',label='TCS') plt.title("Relation between
Tata Motors, Tata Steel and TCS Volume") plt.xlabel("Year") plt.ylabel("Volume")
plt.legend(title="")
#plt.show()
pg. 27
fig = plt.figure() tcs['MA50'] =
tcs['Open'].rolling(50).mean() tcs['MA200'] =
tcs['Open'].rolling(200).mean()
tcs['Open'].plot(figsize = (15,7))
tcs['MA50'].plot()
tcs['MA200'].plot() plt.legend()
plt.grid()
plt.show()
fig = plt.figure()
tcs['returns'] = (tcs['Close']/tcs['Close'].shift(1)) -1 tata_motors['returns'] =
(tata_motors['Close']/tata_motors['Close'].shift(1))-1 tata_steel['returns'] =
(tata_steel['Close']/tata_steel['Close'].shift(1)) - 1 tcs['returns'].hist(bins = 100, label =
'TCS', alpha = 0.5, figsize = (15,7)) tata_motors['returns'].hist(bins = 100, label =
'tata_motors', alpha = 0.5) tata_steel['returns'].hist(bins = 100, label = 'tata_steel', alpha
= 0.5) plt.legend() plt.show() 
