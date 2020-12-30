from flask import Flask, jsonify
import db
from prettify_db_output import prepare_results_from_db

app = Flask(__name__)


@app.route("/")
def home():
    return '''API Usage:
- view_all_articles     --> /articles/all
- view specific article --> /atricles/article_id
- add new article       --> /atricles/add_new
- edit article          --> /atricles/modify
...
'''


@app.route("/articles/all")
def view_all_articles():
    articles = [article for article in prepare_results_from_db()]
    return jsonify(articles)


@app.route("/articles/<article_id>")
def view_articles_by_id(article_id):
    articles = [article for article in db.view_articles_for_specific_id(article_id)]
    return jsonify(articles)


if __name__ == "__main__":
    app.run(debug=True)
