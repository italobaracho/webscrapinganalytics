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
├── img
├── README.md
├── info_games.csv
├── requirements.txt
├── steamdb.ipynb
└── steamdb.py
````

*   img - Pastas das imagens.
*   README.md - Documentação do projeto.
*   info_games.csv - Arquivos gerado pelo script python com os dados da SteamDB.
*   steamdb.ipynb - Notebook com desenvolvimento do Web Scraping do SteamDB.
*   steamdb.py - Neste arquivo contem o mesmo conteudo do notebook, pos o GitHub vem apresentando problemas na visualização do notebook.

## Conexão com o Google Cloud com o serviço PaaS o "BigQuery"

Foi realizado a criação de projeto no _**Google BigQuery**_ com a criação de um dataset _**steamdb**_ e uma tabela _**gameplay**_.

<p align=center>
  <img src="https://raw.githubusercontent.com/italobaracho/webscrapinganalytics/main/img/03.png" width="80%">
</p>

## Conexão com o Google Sheets

No armazenamento dos dados no _**BigQuery**_" fiz a integração nativa com o _**Google Sheets**_" que trouxe todos os dados armazenados, e possível também com essa integração schedular para atualização dos dados. 

### Link do Sheets:

[Google Sheets](https://docs.google.com/spreadsheets/d/16UPfMtGUG3YTlfv-oJdrl9gGYxZFpnRHEMBfxlv-n_E/edit?usp=sharing)