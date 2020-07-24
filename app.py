from flask import Flask, jsonify
from deposit_funds import deposit_funds
from deposit_funds import get_deposit_account
import requests
app = Flask(__name__)

@app.route("/", methods = ['GET'] )
def func():
    return jsonify({"message": "Hello World"})

@app.route("/deposit", methods = ['GET'])
def deposit_function():
    resp = deposit_funds()
    #resp = get_deposit_account()
    return jsonify(resp)

if __name__ == '__main__':
    app.run(debug=True)
