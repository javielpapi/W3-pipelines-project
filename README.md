# Project: Data Pipeline Analyzing Stocks and Crypto Currencies

## Overview

The goal of this project was to practice what we have learned so far in class. For this project I decided to start with a database of cryptocurrencie prices, and enhanced it with the yahoo finance API. 

For this project I chose to explore the relationship between Microsoft, Apple, Gamestop, the S&P500, Bitcoin, and Etherum was.


### I explored my data set, found some interesting relationships between the assets, and ranked them in terms of risk & return using the Sharpe Ratio.



![image](https://user-images.githubusercontent.com/1562979/114416612-c3663b00-9ba8-11eb-84f3-987a6a6f801f.png)



## Technical Requirements

The technical requirements for this project are as follows:

* You must construct a data pipeline with the majority of your code wrapped in functions.
* The following data pipeline stages should be covered: acquisition, wrangling, analysis, and reporting.
* You must demonstrate all the topics we covered in the chapter (functions, list comprehensions, string operations, etc) in your processing of the data.
* There should be some data set that gets imported and some result that gets exported.
* Your code should be saved in a Python executable file (.py), your data should be saved in a folder named data or src, and your results should be saved in a folder named output.
* You should also include a README.md file that describes the steps you took and your thought process as you built your data pipeline.

## Module Requeriements:
- import requests 
- import json
- import os
- from dotenv import load_dotenv
- import pandas as pd
- import time
- import seaborn as sns
- import numpy as np
- from datetime import datetime
- import matplotlib.pyplot as plt

## File Glossary:

### your_code :
#### - Clean Up and Enrichment (V_final).ipynb 
        - where we use our functions to extract and clean the data set.
#### - Visualizing Clean Data (v_final).ipynb
        - where we visualize the data we have cleaned
#### - Analysis of 5 year asset prices.ipynb
        - Where we tell a story about the insights that we gathered. We figure out what the best investment was!   
#### functions.py :
- this document contains the functions that where used for data cleaning. 
- We use functions to calculate the price index based on the first day of the data set, as well as to calculate the previous close, change timestamp data to datetime, and calculate the day to day return of both cryptocurrencies and stock market assets. 
#### Download_data.py : 
- this document contains functions used to extract a data set from kaggle as well as extract stock information using a yahoo finance API.
## data :
- contains the csv data extracted from Kaggle as well as our own dataframes and sub data frames used to plot.
## Graphs: 
- Contains all the plots and visualizations that we used to analyze.



![image](https://user-images.githubusercontent.com/1562979/114416485-a3cf1280-9ba8-11eb-8266-053782f4e4f2.png)

![image](https://user-images.githubusercontent.com/1562979/114416873-045e4f80-9ba9-11eb-962d-afdce40ea53b.png)
