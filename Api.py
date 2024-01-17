import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

#Construindo as funcionalidades
@app.route('/')
def homepage():
  return 'API ta no ar'

@app.route('/pegarvendas')
def pegarvendas():
  tabela = pd.read_csv('teste de api.csv')
  total_vendas = tabela['Vendas'].sum()
  resposta = {'total_vendas': total_vendas}
  return jsonify(resposta)
  


#Rodar a API
app.run(host='0.0.0.0')
