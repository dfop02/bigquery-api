# Python Bigquery
Um simples Python Flask API para consultar Google Cloud Bigquery

[Inglês](readme.md) | [Português](readme.pt-BR.md)

## Requisitos

- Python 3.11.x

## Setup

1. Clone este projeto do Github com `git clone git@github.com:dfop02/bigquery-api.git`
2. Instale a versão correta do python em `.python-version` utilizando algum versionador ou diretamente baixando do [site oficial](https://www.python.org/downloads/).
3. Execute `pip install -r requirements.txt`
4. Antes de rodar o projeto você precisa de uma conta de serviço, para ler como gerar uma, [clique aqui](https://developers.google.com/workspace/guides/create-credentials#create_credentials_for_a_service_account). Depois de gerar, bote o arquivo credentials.json no root do projeto, caso altere o nome do arquivo, lembre de alterar também ele também no .env.
5. Agora basta rodar o app `python app.py`

## Teste / Lint

Se quiser usar os testes ou lint no projeto, primeiro deve instalar as dependencias de dev usando `pip install -r requirements_test.txt`

Depois de instalar as dependencias de dev, pode rodar eles usando:
- Testes => `pytest`.
- Lint => `pylint app.py`

## Fontes / Links / Docs
Sugestão de links como fontes de leitura que vão lhe ajudar a entender melhor o funcionamento do projeto e suas ferramentas

#### Sobre Bigquery
- [Create credentials.json for a service account](https://developers.google.com/workspace/guides/create-credentials#create_credentials_for_a_service_account)
- [Flask + Bigquery](https://medium.com/@akhilasaineni7/backend-pagination-with-flask-and-google-bigquery-c366626d74e6)
- [Google Cloud Bigquery - Python](https://codelabs.developers.google.com/codelabs/cloud-bigquery-python#0)
- [Queries on Bigquery](https://chartio.com/resources/tutorials/how-to-implement-sqls-like-operator-in-google-bigquery/)

#### Sobre JWT
- [PyJWT](https://github.com/jpadilla/pyjwt)
- [Flask + JWT](https://medium.com/@hedgarbezerra35/api-rest-com-flask-autenticacao-25d99b8679b6)

## Autor

[Diogo Fernandes](https://github.com/dfop02)
