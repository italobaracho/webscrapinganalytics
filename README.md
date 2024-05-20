# Execução do Web Scraping

## Extração dos dados da SteamDB na aba "Sales"

A extração foi realizada com sucesso da web na [steam](https://steamdb.info/sales/), porém teve alguns impercilhos para executar essa extração por conta do bloqueio na pagina na parte do "sales" tive que desenvolver passar os parametros no cabeçalho para resolver o problema do erro 403

## Arquitetura do projeto

<p align=center>
  <img src="https://raw.githubusercontent.com/italobaracho/webscrapinganalytics/main/img/01.png" width="30%">
</p>

## Requesitos para o projeto:

Python
Pandas
Warnings
Requests
BeautifulSoup
BigQuery
Service Account
DateTime
to_gbq

## Instalações e Bibliotecas:

# Instale o Python 
```
E logo em seguida execute o comando para instalar todas as libs do projeto
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

## Conexão com o Google Cloud com o serviço PaaS o "BigQuery"

Criamos o dataset na nuvem, em seguida criei as credenciais na "Contas de Serviço" para ter acesso a chave, identificação das tabelas e foi gerado um documento "Json" que contem todos os acessos das chaves privadas para fazer a devida conexão com o "BigQuery"

## Conexão com o Google Sheets

No armazenamento dos dados no "BigQuery" fiz a integração nativa com o "Google Sheets" que trouxe todos os dados do armazenamento do big, e podemos também com essa integração schedular pra posteriomente atualização dos dados 

## Estrutura do Projeto

````
.
├── README.md
├── info_games.csv
├── requirements.txt
├── steamdb.ipynb
└── steamdb.py
````

### Link do Sheets:

[Google Sheets](https://docs.google.com/spreadsheets/d/16UPfMtGUG3YTlfv-oJdrl9gGYxZFpnRHEMBfxlv-n_E/edit?usp=sharing)

### Considerações finais:


