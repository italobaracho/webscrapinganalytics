# Impotando bibliotecas.
import time
import warnings
import requests
import pandas as pd

from datetime import datetime
from bs4 import BeautifulSoup
from google.cloud import bigquery
from google.oauth2 import service_account
from pandas_gbq import to_gbq

warnings.filterwarnings("ignore")


# Parâmetros passados para o headers, problemas como 403.
request_headers = {
    'authority': 'steamdb.info',
    'method': 'GET',
    'path': '/sales/',
    'scheme': 'https',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Dnt': '1',
    'Referer': 'https://steamdb.info/sales/',
    'Sec-Ch-Ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': 'macOS',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

# URL request ao STEAMDB.
URL = 'https://steamdb.info/sales/'

# Lista para armazenar infomações.
game_play = []

try:
    # Realizando raspagem no site.
    pagina = requests.get(URL, headers=request_headers)
    raspagem = BeautifulSoup(pagina.text, "html.parser")

    # Verificando resquest foi realizado com sucesso.
    if pagina.status_code == 200:
        # Buscando tabela dos Games no html.
        print('Status Code:', pagina.status_code)
        tabela = list(raspagem.find_all('tr'))

        # Percorendo e capturando informações da tabela de games.
        for x_game in range(1,len(tabela)):
            game_name = tabela[x_game].find_all('td')[2].a.text
            game_descont = tabela[x_game].find_all('td')[3].text
            game_price = tabela[x_game].find_all('td')[4].text
            game_rating = tabela[x_game].find_all('td')[5].text
            game_release = tabela[x_game].find_all('td')[6].text
            game_ends = datetime.fromtimestamp(int(tabela[x_game].find_all('td')[7]['data-sort']))
            game_started = datetime.fromtimestamp(int(tabela[x_game].find_all('td')[8]['data-sort']))

            # Adicionando informações a lista.
            game_play.append(dict(
                    NAME=game_name,
                    DESCONT=game_descont,
                    PRICE=game_price,
                    RATING=game_rating,
                    RELEASE=game_release,
                    ENDS=game_ends,
                    STARTED=game_started
            ))
    elif pagina.status_code != 200:
        print('ERRO na busca dos dados:', pagina.status_code)
        time.sleep(10)
except Exception as err:
    print('Erro na execução')

# Verificando primeiro registro da lista.
game_play[0]

# Criando data frame para verificar dados e análises.
info_games = pd.DataFrame.from_dict(game_play)
info_games.head(15)

# Verificando quantidade de jogos raspados.
len(game_play)

info_games.shape

# Gerando CVS para importa no Google BigQuery.
info_games.to_csv("info_games.csv", index=False)

# Credenciais para conexão com GoogleBigquery.
credencial = service_account.Credentials.from_service_account_file(
    r'C:\Users\italo\Downloads\disco-idea-423616-n5-2e4ca0b0b00a.json',
    scopes = ['https://www.googleapis.com/auth/bigquery']
)

# Enviando dados para BigQuery.
info_games.to_gbq(
    destination_table='disco-idea-423616-n5.steamdb.gameplay',
    project_id='disco-idea-423616-n5',
    if_exists='replace',
    credentials=credencial
)
