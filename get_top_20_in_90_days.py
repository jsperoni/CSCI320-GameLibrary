from db_config import execute_query

# 7776000 is 90 days in epoch time.
def get_top_20_in_90_days():
    query = ("""
SELECT title
FROM game
    NATURAL JOIN
    (   SELECT game_id, SUM(EXTRACT(EPOCH FROM (end_time - start_time))) / 10.0 * COUNT(DISTINCT player_id) AS score
        FROM plays
        WHERE EXTRACT(EPOCH FROM (CURRENT_DATE - start_time)) BETWEEN 0 AND 7776000
        GROUP BY game_id
    ) AS p
ORDER BY score DESC
LIMIT 20
             """)
    return execute_query(query)

if __name__ == '__main__':
    get_top_20_in_90_days()
