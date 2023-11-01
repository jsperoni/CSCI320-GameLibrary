from db_config import execute_query

# extract epoch based on # https://www.postgresql.org/docs/8.1/functions-datetime.html
def search_game_collections(collection_id):
    sql_command = """
    SELECT
        g.game_id,
        g.title,
        g.esrb
    FROM
        game g
    JOIN
        game_collection gc ON gc.game_id = g.game_id
     WHERE
        gc.collection_id = %s
    GROUP BY
        g.game_id, g.title, g.esrb
    ORDER BY
        g.game_id DESC
    """
    return execute_query(sql_command, params=(collection_id,))

if __name__ == '__main__':
    print(search_game_collections(collection_id=504))