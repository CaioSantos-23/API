###Conversor de moeada com API###

import requests
import json

def obter_cotacoes():
    cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    cotacoes = cotacoes.json()
    cotacao_dolar = float(cotacoes['USDBRL']['bid'])
    cotacao_euro = float(cotacoes['EURBRL']['bid'])
    return cotacao_dolar, cotacao_euro

def converter_para_dolar_e_euro(valor_em_reais, cotacao_dolar,cotacao_euro):
    valor_em_dolar = valor_em_reais / cotacao_dolar
    valor_em_euro = valor_em_reais / cotacao_euro
    return valor_em_dolar, valor_em_euro

cotacao_dolar, cotacao_euro = obter_cotacoes()

real = float(input('Digite o real: '))

valor_dolar, valor_euro = converter_para_dolar_e_euro(real, cotacao_dolar, cotacao_euro)

print(f'{real} BRL é aproximadamente {valor_dolar:.2f} USD')
print(f'{real} BRL é aproximadamente {valor_euro:.2f} EUR')

