from flask import Flask, jsonify, request
from validate_input import validate_input
import db

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return '''<pre>API Usage:
- view_all_articles                   --> /articles/all [GET]
- view specific article               --> /articles/<article_id> [GET]
- view main(current) article          --> /articles/<article_id>/main [GET]
- add new article                     --> /atricles/add [POST]
Requests should have the following structure:
{
 "id": 1,
 "is_main": 1,
 "text": "Body of the article",
 "title": "First Article",
 "version": 1
}
- make any version of the page 'main' --> /articles/make_main [POST]
Use art_id and version in query parameters to specify which version will be 'main'
</pre>'''


@app.route("/articles/all", methods=["GET"])
def view_all_articles():
    articles = db.view_all_articles()
    return jsonify(articles)


@app.route("/articles/<article_id>", methods=["GET"])
def view_articles_by_id(article_id):
    if 'version' in request.args:  # if ?version=version_numb is present in query, specific article will be shown
        articles = db.view_specific_version_for_article(article_id, request.args['version'])
        return jsonify(articles)
    else:  # otherwise, all articles will be shown
        articles = db.view_articles_for_specific_id(article_id)
        return jsonify(articles)


@app.route("/articles/<article_id>/main", methods=["GET"])  # will represent last(main) version of the page
def view_main_article(article_id):
    articles = db.view_main_article(article_id)
    return jsonify(articles)


@app.route('/articles/add', methods=['POST'])
def add_article():
    if validate_input(request.json):
        result = db.add_new_article(request.json)  # will return None if everythong's OK
        db.automatically_set_is_main_flag(request.json['id'])
        if result is not None:
            return jsonify(str(result))

        return jsonify('OK')

    else:
        return jsonify("Insufficient arguments")


@app.route("/articles/make_main", methods=["POST"])
def make_main():
    if 'art_id' and 'version' in request.args:
        db.manually_set_is_main_flag(article_id=request.args['art_id'], version=request.args['version'])
    return jsonify('OK')


if __name__ == "__main__":
    app.run(debug=True)
