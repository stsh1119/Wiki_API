import db


def prepare_results_from_db() -> list:
    parsed_articles = []

    for db_tuple in db.view_all_articles():  # getting tuple data from database and forming dictionary
        dict_output = {'id': db_tuple[0],
                       'title': db_tuple[1],
                       'text': db_tuple[2],
                       'version': db_tuple[3],
                       'is_main': db_tuple[4]
                       }
        parsed_articles.append(dict_output)  # creating a list to return

    return parsed_articles
