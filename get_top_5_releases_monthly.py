from db_config import execute_query

# 2592000 is 30 days in epoch time.
def get_top_5_releases_monthly():
    query = ("""
             SELECT p.game_id, SUM(EXTRACT(EPOCH FROM (end_time - start_time))) AS total_time, AVG(r.rating) AS average_rating
             FROM plays p JOIN rates r on p.game_id = r.game_id
             WHERE EXTRACT(EPOCH FROM (CURRENT_DATE - start_time)) < 2592000
             GROUP BY p.game_id
             ORDER BY total_time DESC, average_rating DESC
             LIMIT 5
             """)
    return execute_query(query)

if __name__ == '__main__':
    get_top_5_releases_monthly()
