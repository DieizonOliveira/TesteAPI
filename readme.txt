README - Operadoras de Plano de Saúde

Este projeto consiste em um sistema para buscar operadoras de planos de saúde, utilizando um frontend em Vue.js e um backend em Flask.

📌 Tecnologias Utilizadas

Frontend (Vue.js):

Vue.js 3

Axios

HTML, CSS (Scoped Styles)

Backend (Flask):

Python 3

Flask

Flask-CORS

Pandas (se estiver usando CSV para armazenar os dados)

🖥️ Configuração do Backend (Flask)

🔧 Requisitos:

Python 3.8+

pip instalado

🔥 Instalação e Execução:

Clone este repositório:


Crie e ative um ambiente virtual no repositório backend.

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows

Instale as dependências:

pip install -r requirements.txt

Inicie o servidor Flask:

python app.py

O servidor será iniciado em http://127.0.0.1:5000/

🔄 Endpoints da API:

GET /buscar?query=<termo> - Busca operadoras por nome, CNPJ ou cidade.

🌐 Configuração do Frontend (Vue.js)

🔧 Requisitos:

Node.js 16+

Gerenciador de pacotes npm ou yarn

🔥 Instalação e Execução:

Navegue até a pasta do frontend:

cd busca-operadora

Instale as dependências:

npm install

Inicie o servidor de desenvolvimento:

npm run serv

O frontend será iniciado em http://localhost:8080/

🚀 Uso do Sistema

Acesse http://localhost:8080/.

Digite o nome, CNPJ ou cidade da operadora no campo de pesquisa.

Clique em "Pesquisar" para buscar os dados.

Os resultados serão exibidos em uma tabela.

Clique em "Limpar" para resetar a pesquisa.
