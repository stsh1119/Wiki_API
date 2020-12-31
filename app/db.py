import sqlite3
from prettify_db_output import prepare_results_from_db


def view_all_articles() -> list:
    conn = sqlite3.connect("articles.db")
    with conn:
        cursor = conn.cursor()
        query_result = cursor.execute("select * from wiki_page").fetchall()
        result = prepare_results_from_db(query_result)
        return result


def view_articles_for_specific_id(article_id: str) -> list:
    conn = sqlite3.connect("articles.db")
    with conn:
        cursor = conn.cursor()
        query_result = cursor.execute("select * from wiki_page where article_id = ?", article_id).fetchall()
        result = prepare_results_from_db(query_result)
        return result


def view_specific_version_for_article(article_id: str, version: int) -> list:
    conn = sqlite3.connect("articles.db")
    with conn:
        cursor = conn.cursor()
        query_result = cursor.execute("""select *
                                         from wiki_page
                                         where article_id = ?
                                         and version = ?""",
                                      (article_id, version)
                                      ).fetchall()
        result = prepare_results_from_db(query_result)
        return result


def view_main_article(article_id: str) -> list:
    conn = sqlite3.connect("articles.db")
    with conn:
        cursor = conn.cursor()
        query_result = cursor.execute("""select *
                                        from wiki_page
                                        where article_id = ?
                                        and is_main = TRUE
                                        and version = (select max(version)
                                                            from wiki_page
                                                            where article_id = ?
                                                            group by article_id)""",
                                      (article_id, article_id)).fetchall()

        result = prepare_results_from_db(query_result)
        return result


def add_new_article(article_info: dict) -> None:
    conn = sqlite3.connect("articles.db")
    with conn:
        cursor = conn.cursor()
        try:
            cursor.execute("""insert into wiki_page(article_id, title, text, version, is_main)
                            values(:id, :title, :text, :version, :is_main)""",
                           {
                            'id': article_info['id'],
                            'title': article_info['title'],
                            'text': article_info['text'],
                            'version': article_info['version'],
                            'is_main': article_info['is_main']
                            }
                           )
        except sqlite3.IntegrityError as err:
            return err


def automatically_set_is_main_flag(article_id: str):
    conn = sqlite3.connect("articles.db")
    with conn:
        cursor = conn.cursor()
        cursor.execute("""update wiki_page
                          set is_main = 0
                          where article_id = ?
                          and version != (select max(version)
                                          from wiki_page
                                          where article_id = ?
                                          group by article_id)""",
                       (article_id, article_id)
                       )


def manually_set_is_main_flag(article_id: str, version: int) -> None:
    conn = sqlite3.connect("articles.db")
    with conn:
        cursor = conn.cursor()
        cursor.execute('update wiki_page set is_main = 0 where article_id = ?', article_id)
        cursor.execute('update wiki_page set is_main = 1 where article_id = ? and version = ?', (article_id, version))
