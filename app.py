from flask import Flask, request, url_for
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import json
from components.log import log
app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db'


@app.route('/post/<name>', methods=['POST'])
def post(name):

    request_method = request.method
    query_params_dict = request.args
    request_body = request.data
    log(query_params_dict)
    log(name)
    x = json.loads(request_body)
    log(x)

    return dict({'status': 200, 'query_param': query_params_dict, 'body': x, 'paramters': name})


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

db = SQLAlchemy(app)
db.session


class Territories(db.Model):
    TerritoryID = db.Column(db.Integer, primary_key=True, nullable=False)
    TerritoryDescription = db.Column(db.String(15), nullable=False)
    region = relationship('Region')


class Region(db.Model):
    RegionID = db.Column(db.Integer, primary_key=True, nullable=False)


data = Territories.query.all()


log(data)

if __name__ == '__main__':
    app.run()
