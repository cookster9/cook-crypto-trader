from flask import Flask, jsonify
from deposit_funds import deposit_funds
from check_stats import check_stats

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

if __name__ == '__main__':
    app.run(debug=True)
