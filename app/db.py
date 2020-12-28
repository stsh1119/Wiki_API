import sqlite3


def view_all_articles() -> list:
    conn = sqlite3.connect("articles.db")
    with conn:
        cursor = conn.cursor()
        result = cursor.execute("select * from wiki_page").fetchall()
        return result


def view_articles_for_specific_id(article_id) -> list:
    conn = sqlite3.connect("articles.db")
    with conn:
        cursor = conn.cursor()
        result = cursor.execute("select * from wiki_page where article_id = ?", article_id).fetchall()
        return result


# print(view_articles_for_specific_id('1'))
