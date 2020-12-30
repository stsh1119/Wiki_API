import sqlite3


def view_all_articles() -> list:
    conn = sqlite3.connect("articles.db")
    with conn:
        cursor = conn.cursor()
        result = cursor.execute("select * from wiki_page").fetchall()
        return result


def view_articles_for_specific_id(article_id: str) -> list:
    conn = sqlite3.connect("articles.db")
    with conn:
        cursor = conn.cursor()
        result = cursor.execute("select * from wiki_page where article_id = ?", article_id).fetchall()
        return result


def view_specific_version_for_article(article_id: str, version: int) -> list:
    conn = sqlite3.connect("articles.db")
    with conn:
        cursor = conn.cursor()
        result = cursor.execute("""select *
                                   from wiki_page
                                   where article_id = ?
                                   and version = ?""",
                                (article_id, version)
                                ).fetchall()
        return result


def view_main_article(article_id: str) -> list:
    conn = sqlite3.connect("articles.db")
    with conn:
        cursor = conn.cursor()
        result = cursor.execute("""select *
                                   from wiki_page
                                   where article_id = ?
                                   and is_main = TRUE
                                   and version = (select max(version)
                                                    from wiki_page
                                                    where article_id = ?
                                                    group by article_id)""",
                                (article_id, article_id)).fetchall()
        return result

