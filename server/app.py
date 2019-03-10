from flask import Flask, jsonify, request
from db import results, results_adv
from create_table import update

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello, Welcome to Advanced Python package manager</h1>"

@app.route('/search')
def search():
    text = request.args.get('q')
    update()
    data = results(text)

    print(data)
    return jsonify({
        'code': 200,
        'data': data
    })

@app.route('/search/adv')
def search_advance():
    text = request.args.get('q')
    update()
    data = results_adv(text)

    print(data)
    return jsonify({
        'code': 200,
        'data': data
    })

if __name__ == "__main__":
	app.run(host="0.0.0.0")