import os as os

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