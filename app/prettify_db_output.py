def prepare_results_from_db(raw_db_output: list) -> list:
    parsed_articles = []

    for db_tuple in raw_db_output:  # getting tuple data from database and forming dictionary
        dict_output = {'id': db_tuple[0],
                       'title': db_tuple[1],
                       'text': db_tuple[2],
                       'version': db_tuple[3],
                       'is_main': db_tuple[4]
                       }
        parsed_articles.append(dict_output)  # creating a list to return

    return parsed_articles
