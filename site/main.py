from flask import Flask
from flask import request


app = Flask(__name__)

@app.route('/')
def hello_world():
    return ':)'

@app.route('/request', methods=['GET'])
def send_data():
    searchword = request.args.get('key', '')
    return searchword