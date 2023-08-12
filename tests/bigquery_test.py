import sys
import json
from unittest.mock import patch
from os.path import dirname
sys.path.append(dirname(dirname(__file__)))
from app import app

app.config.update({
    "TESTING": True,
})

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

bq_query_response = [
    {
        'ID': 95258711020,
        'NAME': 'Test',
        'PROJETS': 'project A',
        'COMPANY': 'company F',
        'COMPANYLEADER': 'Foo'
    }
]

def test_invalid_json_format():
    response = app.test_client().post('/api/v1/bigquery')
    res = json.loads(response.data.decode('utf-8')).get('result')

    assert response.content_type == 'application/json'
    assert response.status_code == 406
    assert res == 'Invalid Format, please use JSON as request format.'

def test_valid_json_format():
    data = {'name': 'test'}
    with patch('google.cloud.bigquery.client.Client.query') as mock_get:
        mock_get.return_value = bq_query_response
        response = app.test_client().post('/api/v1/bigquery', json=data, headers=headers)

    assert response.content_type == 'application/json'
    assert response.status_code == 200

def test_success_bq_consult():
    data = {'name': 'test'}
    with patch('google.cloud.bigquery.client.Client.query') as mock_get:
        mock_get.return_value = bq_query_response
        response = app.test_client().post('/api/v1/bigquery', json=data, headers=headers)

    res = json.loads(response.data.decode('utf-8')).get('result')

    assert response.content_type == 'application/json'
    assert response.status_code == 200
    assert res == bq_query_response

def test_failure_bq_consult():
    data = {'name': 'bloom'}
    with patch('google.cloud.bigquery.client.Client.query') as mock_get:
        mock_get.return_value = []
        response = app.test_client().post('/api/v1/bigquery', json=data, headers=headers)

    res = json.loads(response.data.decode('utf-8')).get('result')

    assert response.content_type == 'application/json'
    assert response.status_code == 200
    assert res == []
