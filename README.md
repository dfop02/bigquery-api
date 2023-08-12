# Python Bigquery
A simple Python Flask API to consult Google Cloud Bigquery

[English](readme.md) | [Portuguese](readme.pt-BR.md)

## Requirements

- Python 3.11.x

## Setup

1. Clone this repo from Github with `git clone git@github.com:dfop02/bigquery-api.git`
2. Install the correct python version in `.python-version` using any python manager or directly download from [official website](https://www.python.org/downloads/).
3. Execute `pip install -r requirements.txt`
4. Before run the code you must have an service account, you can read how generate it [here](https://developers.google.com/workspace/guides/create-credentials#create_credentials_for_a_service_account). After generate, put the credentials.json on project's root, if you change the filename, make sure you changed in .env too.
5. Now just run the app using `python app.py`

## Test / Lint

If you want use tests or lint on this project, first you must need install the test dependences using `pip install -r requirements_test.txt`

After install the test dependences, you can run by using:
- Tests => `pytest`.
- Lint => `pylint app.py`

## Fonts / Links / Docs
Suggestion of links, fonts to read about that you help you to learn more about how this code works and how the services we're using works.

#### About Bigquery
- [Create credentials.json for a service account](https://developers.google.com/workspace/guides/create-credentials#create_credentials_for_a_service_account)
- [Flask + Bigquery](https://medium.com/@akhilasaineni7/backend-pagination-with-flask-and-google-bigquery-c366626d74e6)
- [Google Cloud Bigquery - Python](https://codelabs.developers.google.com/codelabs/cloud-bigquery-python#0)
- [Queries on Bigquery](https://chartio.com/resources/tutorials/how-to-implement-sqls-like-operator-in-google-bigquery/)

#### About JWT
- [PyJWT](https://github.com/jpadilla/pyjwt)
- [Flask + JWT](https://medium.com/@hedgarbezerra35/api-rest-com-flask-autenticacao-25d99b8679b6)

## Author

[Diogo Fernandes](https://github.com/dfop02)
