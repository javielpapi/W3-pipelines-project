from datetime import datetime

#definimos una funcion que convierte un valor timestamp a un valor datetime usando un apply
#la funcion necesita tener datetime importado
def ts_to_dt(df, column, new_column):
    df[str(new_column)] = df[column].apply(datetime.fromtimestamp)
    return df

# We define some functions that will help us create previous close functions for crypto
def crypto_prev_close (df):
    for v in range(1, len(df)):
        df.loc[v, 'previousClose'] = df.loc[v - 1, 'Close']
    return df

def crypto_return(df):
    df['percent_change'] = df['Close'].pct_change()
    return df

#We Notice that the data frame is missing values in the previous close column
#we create a function that calculates the value using the previous rows close value
def previous_close(df):
    for v in range(1, len(df)):
        df.loc[v, 'previousClose'] = df.loc[v - 1, 'close']
    return df

#We create a function to create a percentage change column by inputing a dataframe from the yahoo finance api
def percent_change(df):
    df['percent_change'] = df['close'].pct_change()
    return df

# We create a new column that tracks the growth of the stock since the first day in our dataframe, 
#this alows us to bettter compare across a big range of prices
# this is the function for stocks:
def base_price(df):
    for v in range(0, len(df)):
        df.loc[v, 'price_index'] = df.loc[v, 'close'] / df.loc[0, 'close']
    return df

#We create the same function with different columns to iterate over our crypto data
def crypto_index(df):
    for v in range(0, len(df)):
        df.loc[v, 'price_index'] = df.loc[v, 'Close'] / df.loc[0, 'Close']
    return df


