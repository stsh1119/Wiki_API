import sqlite3


def add_new_article(title: str, body: str, is_main=1) -> None:
    conn = sqlite3.connect("articles.db")
    with conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""insert into wiki_page(title, text, is_main)
                           values( '{title}', '{body}', {is_main})"""
        )
        conn.commit()


def view_all_articles() -> list:
    conn = sqlite3.connect("articles.db")
    with conn:
        cursor = conn.cursor()
        result = cursor.execute("select * from wiki_page").fetchall()
        return result


wiki_pages = [
    {
        "id": 0,
        "title": "A Fire Upon the Deep",
        "author": "Vernor Vinge",
        "first_sentence": "The coldsleep itself was dreamless.",
        "year_published": "1992",
    },
    {
        "id": 1,
        "title": "The Ones Who Walk Away From Omelas",
        "author": "Ursula K. Le Guin",
        "first_sentence": "With a clamor of bells that set the swallows soaring, \
the Festival of Summer came to the city Omelas, bright-towered by the sea.",
        "published": "1973",
    },
    {
        "id": 2,
        "title": "Dhalgren",
        "author": "Samuel R. Delany",
        "first_sentence": "to wound the autumnal city.",
        "published": "1975",
    },
]
