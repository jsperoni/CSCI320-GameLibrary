from db_config import execute_query

def get_top_20_from_followers(player_id):
    query = (f"""
            
            SELECT p.game_id, SUM(EXTRACT(EPOCH FROM (end_time - start_time))) AS total_time, AVG(r.rating) AS average_rating
            FROM follows f JOIN plays p ON f.follower_id = p.player_id JOIN rates r ON r.game_id = p.game_id
            WHERE f.player_id = {player_id}
            GROUP BY p.game_id
            ORDER BY total_time DESC, average_rating DESC
            LIMIT 20
             """)
    print(execute_query(query))

if __name__ == '__main__':
    get_top_20_from_followers(1608)
