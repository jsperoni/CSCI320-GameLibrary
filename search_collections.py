from db_config import execute_query

# extract epoch based on # https://www.postgresql.org/docs/8.1/functions-datetime.html
#
# was getting error below when i wasn't type casting
# [42883] ERROR: function mod(double precision, integer) does not exist
# Hint: No function matches the given name and argument types.
# You might need to add explicit type casts. Position: 220
def search_collection(player_id):
    sql_command = """
    SELECT
       c.collection_id,
       c.name,
       COALESCE(COUNT(DISTINCT gc.game_id), 0) AS game_count,
       COALESCE(FLOOR(SUM(EXTRACT(EPOCH FROM (P.end_time - P.start_time)) / 3600)), 0) AS hours_played,
       COALESCE(FLOOR((SUM(EXTRACT(EPOCH FROM (P.end_time - P.start_time)))::integer %% 3600) / 60), 0) AS minutes_played
    FROM
        collection c
    LEFT JOIN
        game_collection gc ON c.collection_id = gc.collection_id
    LEFT JOIN
        plays p ON gc.game_id = p.game_id AND c.player_id = p.player_id
    WHERE
        c.player_id = %s
    GROUP BY
        c.collection_id, c.name 
    ORDER BY
        c.name ASC;
    """
    return execute_query(sql_command, params=(player_id,))

if __name__ == '__main__':
    print(search_collection(player_id=2596))