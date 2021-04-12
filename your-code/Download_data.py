import os as os
import requests 
import json

def download_data_sets():
    '''Downloads a dataset from kaggle and only keeps the csv in your data file. Beware of your own data structure:
    this creates a data directory and also moves all the .csv files next to your jupyter notebooks to it.
    Takes: url from kaggle
    Returns: a folder with the downloaded csv
    '''
    url = input('introduce the link to kaggle dataset: ')

    #Gets the name of the dataset.zip
    endopint = url.split("/")[-1]
    user = url.split("/")[-2]

    download = f"kaggle datasets download -d {user}/{endopint}; say -v Monica 'descargando'"
    decompress = f"tar -xzvf {endopint}.zip; say -v Monica 'descomprimiendo'"
    delete = f"rm -rf {endopint}.zip; say -v Monica 'borrando el zip'"
    make_directory = "mkdir data"
    lista = "ls >> archivos.txt"
    for i in [download, decompress, delete, make_directory, lista]:
        os.system(i)
    
    move_and_delete = f"mv *.csv database/; say -v Monica 'moviendo el dataset'"
    return os.system(move_and_delete)


def access_yahoo(url_yahoo, parameters): 
    '''
    Accesses the yahoo finance api with given parameters, uses our key.

    where:
    url_yahoo: the yahoo_api url you will use to connect. 
    for this function to work you need to be using rapid apis low latency yahoo api.

    parameters = a dictionary with the following keys:
    {'symbols': 'TICKERS ex: AAPL, GME, MSFT', 'range':'5y', 'interval':'1d'}
    
    '''
    headers = {
    'x-rapidapi-key': "5978a55496msh35be22b262fe8acp19f68cjsn3abe53806b27",
    'x-rapidapi-host': "yahoo-finance-low-latency.p.rapidapi.com"
    }
    response = requests.request("GET", url_yahoo, headers=headers, params=parameters)

    return response.json()
