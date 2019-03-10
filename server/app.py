from flask import Flask, jsonify
from db import results

app = Flask(__name__)

@app.route('/search')
def search():
    text = request.args.get('q')
    data = results(text)

    print(data)
    return jsonify({
        'code': 200,
        'data': data
    })

if __name__ == "__main__":
	app.run(host="0.0.0.0")