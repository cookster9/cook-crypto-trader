from flask import Flask, jsonify
from deposit_funds import deposit_funds
from check_stats import check_stats
from get_history import get_history

app = Flask(__name__)

@app.route("/", methods = ['GET'] )
def func():
    return jsonify({"message": "Hello World"})

@app.route("/deposit", methods = ['GET'])
def deposit_function():
    amount = 10
    resp = deposit_funds(deposit_amount = amount)
    #resp = get_deposit_account()
    return jsonify(resp)

@app.route("/check", methods = ['GET'] )
def check_stats_func():
    resp = check_stats()
    return jsonify(resp)

@app.route("/hist", methods = ['GET'] )
def get_hist_func():
    resp = get_history()
    return jsonify(resp)

if __name__ == '__main__':
    app.run(debug=True)
