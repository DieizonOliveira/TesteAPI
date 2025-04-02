from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import numpy as np

app = Flask(__name__)
CORS(app)  # Permite requisições do frontend Vue.js

# Carregar o CSV com tratamento de erro
try:
    df = pd.read_csv('Relatorio_cadop.csv', delimiter=';', dtype=str)  # Lê tudo como string
except FileNotFoundError:
    print("Erro: O arquivo 'Relatorio_cadop.csv' não foi encontrado.")
    df = pd.DataFrame()  # Cria um DataFrame vazio para evitar erros

def limpar_nan(dados):
    """Substitui NaN e valores inválidos por None para evitar erro no JSON"""
    return [{k: (None if pd.isna(v) or v == "nan" else v) for k, v in d.items()} for d in dados]

@app.route('/buscar', methods=['GET'])
def buscar():
    query = request.args.get('query', default='', type=str).strip()

    if query and not df.empty:
        # Filtrar os registros que contêm a query (ignorando maiúsculas e minúsculas)
        resultado = df[df.apply(lambda row: row.astype(str).str.contains(query, case=False, na=False).any(), axis=1)]
        return jsonify(limpar_nan(resultado.to_dict(orient='records')))
    
    return jsonify([])  # Retorna uma lista vazia se a query estiver vazia ou se o CSV estiver ausente

if __name__ == '__main__':
    app.run(debug=True)












# from flask import Flask, request, jsonify
# import pandas as pd

# app = Flask(__name__)

# # Carregar o CSV
# df = pd.read_csv('Relatorio_cadop.csv', delimiter=';')

# @app.route('/buscar', methods=['GET'])
# def buscar():
#     # Pegar o parâmetro de busca enviado pelo cliente
#     query = request.args.get('query', default='', type=str)
    
#     # Filtrar os registros com base na query
#     resultado = df[df.apply(lambda row: row.astype(str).str.contains(query, case=False).any(), axis=1)]
    
#     # Retornar os resultados como JSON
#     return jsonify(resultado.to_dict(orient='records'))

# if __name__ == '__main__':
#     app.run(debug=True)
