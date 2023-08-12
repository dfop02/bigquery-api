from os import getenv
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from google.cloud import bigquery

load_dotenv()
app = Flask(__name__)
client = bigquery.Client.from_service_account_json(json_credentials_path=getenv('CREDENTIALS_PATH'))

@app.before_request
def only_json():
    if not request.is_json:
        return jsonify({
            'result': 'Invalid Format, please use JSON as request format.',
            'status_code': 406
        }), 406

    return None

@app.route('/api/v1/bigquery', methods=['POST'])
def home():
    request_json = request.get_json()
    try:
        result = query_to_bigquery(request_json)
        return jsonify({'result': result, 'status_code': 200}), 200
    except Exception as error:
        print(error)
        return jsonify({'result': f'Error: {error}', 'status_code': 400}), 400

def query_to_bigquery(params):
    where = []
    query_parameters = []

    # Currenctly only accept strings as column type
    for key, value in params.items():
        where.append(f'LOWER({key}) = ?')
        query_parameters.append(bigquery.ScalarQueryParameter(None, 'STRING', value.casefold()))

    if not where or not query_parameters:
        return None

    query = f"""
        SELECT *
        FROM `{getenv('BQ_TABLE')}`
        WHERE {' and '.join(where)}
    """

    job_config = bigquery.QueryJobConfig(query_parameters=query_parameters)
    query_job = client.query(query, job_config=job_config)
    records = [dict(row) for row in query_job]
    return records

if __name__ == '__main__':
    app.run(
        debug=(getenv('DEBUG', 'False') == 'True'),
        host=getenv('HOST', '0.0.0.0'),
        port=int(getenv('PORT', '3000'))
    )
