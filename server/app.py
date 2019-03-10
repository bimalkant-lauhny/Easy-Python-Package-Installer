from flask import Flask, jsonify, request
from db import results
from create_table import update

app = Flask(__name__)

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

if __name__ == "__main__":
	app.run(host="0.0.0.0")