from db_config import execute_query

# 2592000 is 30 days in epoch time.

# As of 12/1 no one has played a monthly new release in the 30 days it has been out
# so this query will not return any data.
# Changing all instances of CURRENT_DATE to '2023-04-01' guarantees the query will return
# a value.


def get_top_5_releases_monthly():
    query = ("""
SELECT title, initial_release
FROM game
    NATURAL JOIN
    (   SELECT game_id, SUM(EXTRACT(EPOCH FROM (end_time - start_time))) / 10.0 * COUNT(DISTINCT player_id) AS score
         FROM plays
         WHERE EXTRACT(EPOCH FROM (CURRENT_DATE - start_time)) BETWEEN 0 AND 2592000
         GROUP BY game_id) AS p
    NATURAL JOIN
    (   SELECT game_id, MIN(release_date) AS initial_release
        FROM runs_on
        GROUP BY game_id) AS q
WHERE CURRENT_DATE - initial_release BETWEEN 0 AND 30
ORDER BY score DESC
LIMIT 5
             """)
    return execute_query(query)


if __name__ == '__main__':
    get_top_5_releases_monthly()
