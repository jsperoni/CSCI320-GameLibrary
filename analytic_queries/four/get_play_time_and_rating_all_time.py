from db_config import execute_query

def get_all_play_time_and_rating():
    query = ("""
             SELECT p.game_id, SUM(end_time - start_time) AS total_time, AVG(r.rating) AS average_rating
             FROM plays p JOIN rates r on p.game_id = r.game_id
             GROUP BY p.game_id
             ORDER BY total_time DESC, average_rating DESC
             """)

    print(execute_query(query))

if __name__ == '__main__':
    get_all_play_time_and_rating()
