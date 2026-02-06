import requests

def buscar_cotacao():
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL,ARS-BRL,CHF-BRL"
    resposta = requests.get(url)
    return resposta.json()

dados = buscar_cotacao()#chamada da função/o retorno vira a variavel dados e agora dados é um dicionario [chave][valor]


def buscar_historico_bitcoin():
    url = "https://economia.awesomeapi.com.br/json/daily/BTC-BRL/15"
    resposta = requests.get(url)
    dados = resposta.json()
    precos = [float(item['bid']) for item in dados]
    return precos[::-1]

def converter(valor, cotacao):
    return valor / cotacao
