from flask import Flask, request, jsonify
import db

app = Flask(__name__)


@app.route('/')
def home():
    results = []
    for row in db.view_all_articles():
        result = {'id': row[0],
                  'title': row[1],
                  'text': row[2],
                  'is_current': row[3]
                  }
        results.append(result)
    return jsonify(results)


@app.route('/add_page', methods=['POST'])
def add_page():
    if request.is_json:
        title = request.json.get("title")
        body = request.json.get("body")
        # return request.get_json()
        return f'''{title} --- {body}'''


if __name__ == '__main__':
    app.run(debug=True)
