from db_config import execute_query

# unfinished
def for_you(player_id):
    query = f"""
SELECT DISTINCT player_id
FROM (SELECT player_id,
             SUM((EXTRACT(EPOCH FROM (end_time - start_time))))   AS total_time,
             genre_id,
             ROW_NUMBER() OVER (PARTITION BY player_id, genre_id) AS row_num
      FROM plays p
               NATURAL JOIN game_genre g
               NATURAL JOIN contributor
      WHERE EXTRACT(EPOCH FROM (end_time - start_time)) > 0
      GROUP BY player_id, genre_id
      ORDER BY player_id, total_time DESC) AS sub1
WHERE row_num <= 3
AND genre_id in (
    SELECT

    """
    return execute_query(query, params=(player_id,))

if __name__ == '__main__':
    print(find_following(player_id=2420))