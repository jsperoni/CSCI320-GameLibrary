from db_config import execute_query

# extract epoch based on # https://www.postgresql.org/docs/8.1/functions-datetime.html
def search_collection(player_id):
    sql_command = """
    SELECT
        c.name,
        COUNT(DISTINCT gc.game_id),
        SUM(EXTRACT(EPOCH FROM (p.end_time - p.start_time)) / 3600)
    FROM
        collection c
    JOIN
        game_collection gc ON c.collection_id = gc.collection_id
    LEFT JOIN
        plays p ON gc.game_id = p.game_id AND c.player_id = p.player_id
    WHERE
        c.player_id = %s
    GROUP BY
        c.name
    ORDER BY
        c.name ASC
    """
    return execute_query(sql_command, params=(player_id,))

if __name__ == '__main__':
    print(search_collection(player_id=2596))