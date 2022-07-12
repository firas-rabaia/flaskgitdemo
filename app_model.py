from flask import Flask, request, url_for
from flask_cors import CORS
import json
app = Flask(__name__)
CORS(app)


@app.route('/post/<name>', methods=['POST'])
def post(name):
    request_method = request.method
    query_params_dict = request.args
    request_body = request.data
    log(query_params_dict)
    log(name)
    x = json.loads(request_body)
    log(x)

    return dict({'status': 200, 'query_param': name, 'body': x})


@app.route('/get', methods=['GET'])
def get():
    request_method = request.method
    request_body = request.data
    query_params_dict = request.args
    log(query_params_dict)
    log(request_body)
    return dict({'status': 200, 'data': ''})


with app.test_request_context():
    print(url_for('post', name='firas'))
    print(url_for('get'))


def log(msg):
    print(f'------------------------ {msg=}')


if __name__ == '__main__':
    app.run()
