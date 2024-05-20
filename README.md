# Execução do Web Scraping

## Extração dos dados da SteamDB "Sales"

Foi realizada a extração da web na [steam](https://steamdb.info/sales/), porém teve alguns impercilhos, o site da steamdb não possui "API" e não permite o web scraping porém foi possivel contornar parametrizando o header para realizar requests se passando por um browser está foi a forma que conseguir contornar erro dos tipos 401, 403 e 429. 

<p align=center>
  <img src="https://raw.githubusercontent.com/italobaracho/webscrapinganalytics/main/img/02.jpg" width="80%">
</p>

## Arquitetura do projeto

<p align=center>
  <img src="https://raw.githubusercontent.com/italobaracho/webscrapinganalytics/main/img/01.png" width="50%">
</p>

## Instalações e Bibliotecas:
 
```
pip install -r requirements.txt
```

## Colunas Extraidas:

````
NAME - Nome do jogo
DESCONT	- Desconto atualizado
PRICE - Preço atualizado
RATING	- Avaliação atualizada
RELEASE	- Lançamento dos jogos
ENDS - Quando finaliza a promoção dos jogos
STARTED - Quando começa a promoção dos jogos
````

## Estrutura do Projeto
````
.
├── README.md
├── info_games.csv
├── requirements.txt
├── steamdb.ipynb
└── steamdb.py
````
## Conexão com o Google Cloud com o serviço PaaS o "BigQuery"

Foi realizado a criação de projeto no _**Google BigQuery**_ com a criação de um dataset _**steamdb**_ e uma tabela _**game_play**_.

<p align=center>
  <img src="https://raw.githubusercontent.com/italobaracho/webscrapinganalytics/main/img/03.png" width="80%">
</p>

## Conexão com o Google Sheets

No armazenamento dos dados no "BigQuery" fiz a integração nativa com o "Google Sheets" que trouxe todos os dados do armazenamento do big, e podemos também com essa integração schedular pra posteriomente atualização dos dados 

### Link do Sheets:

[Google Sheets](https://docs.google.com/spreadsheets/d/16UPfMtGUG3YTlfv-oJdrl9gGYxZFpnRHEMBfxlv-n_E/edit?usp=sharing)