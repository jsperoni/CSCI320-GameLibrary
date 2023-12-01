from db_config import execute_query

def get_top_20_from_followers(player_id):
    query = (f"""
SELECT title
FROM game
    NATURAL JOIN
    (
        SELECT game_id, COALESCE(total_time, 0) as time, avg_rating
            FROM
                (
                    SELECT game_id, SUM(EXTRACT(EPOCH FROM (end_time - start_time))) AS total_time
                    FROM follows f
                        JOIN plays p ON f.follower_id = p.player_id
                    WHERE f.player_id = {player_id}
                    GROUP BY game_id
                ) AS p
                NATURAL FULL JOIN
                (
                    SELECT game_id, AVG(rating) AS avg_rating
                    FROM follows f
                              JOIN rates r ON f.follower_id = r.player_id
                    WHERE f.player_id = {player_id}
                    GROUP BY game_id
                ) AS q
    ) AS s
ORDER BY time, avg_rating
LIMIT 20
             """)
    return execute_query(query) 

if __name__ == '__main__':
    get_top_20_from_followers(1608)
