from db_config import execute_query

def find_followers(player_id):
    query = """
    SELECT p.*
    FROM player p
    JOIN follows f ON p.player_id = f.follower_id
    WHERE f.player_id = %s
    """
    return execute_query(query, params=(player_id,))

if __name__ == '__main__':
    print(find_followers(player_id=2420))