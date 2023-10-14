import requests
from flask import Flask, request
import rule

app = Flask(__name__)

@app.route('/', methods=["POST"])

def post_data():
        data = request.get_json()        #getpost返回值
        msg = data['raw_message']     #get消息
        rule.rule()
        return 'OK'

app.run(debug=True, host='127.0.0.1', port=5701)