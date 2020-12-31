from flask import Flask, jsonify, request
import db
# from prettify_db_output import prepare_results_from_db

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return '''API Usage: #! FINISH DESCRIPTION
- view_all_articles     --> /articles/all
- view specific article --> /atricles/article_id
- add new article       --> /atricles/add_new
- edit article          --> /atricles/modify
...
'''


@app.route("/articles/all")
def view_all_articles():
    articles = db.view_all_articles()
    return jsonify(articles)


@app.route("/articles/<article_id>")
def view_articles_by_id(article_id):
    if 'version' in request.args:  # if ?version=version_numb is present in query, specific article will be shown
        articles = db.view_specific_version_for_article(article_id, request.args['version'])
        return jsonify(articles)
    else:  # otherwise, all articles will be shown
        articles = db.view_articles_for_specific_id(article_id)
        return jsonify(articles)


@app.route("/articles/<article_id>/main")  # will represent last(main) version of the page
def view_main_article(article_id):
    articles = db.view_main_article(article_id)
    return jsonify(articles)


if __name__ == "__main__":
    app.run(debug=True)
