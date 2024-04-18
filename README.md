# Flask API - Cadastro Clientes

Projeto construído para o MVP da PUC-Rio.

## Objetivo

A API tem como propósito realizar o controle de carteira de clientes dos corretores de terminadas empresa , possibilitando uma melhor organização dessas relações.

## Requirements

- flask-openapi3 2.1+
- SQLAlchemy 1.4+

# Instalação e Execução

### Instalação

Para instalar as libs python necessárias, após clonar o repositório, no diretório raiz execute o comando:

> pip install -r requirements.txt

### Execução

Para executar a API, no diretório raiz execute o comando:

> flask run --host 0.0.0.0 --port 5000

### Modo de desenvolvimento

Para executar a API em modo de desenvolvimento, no diretório raiz execute o comando:

> flask run --host 0.0.0.0 --port 5000 --reload

## Documentação

Após iniciar a execução da API, a documentação estará disponível acessando a rota padrão:

> http://127.0.0.1:5000/
> Estando disponível as opções de documentação do Swagger, ReDoc e RapiDoc
