from db_config import execute_query

def find_following(player_id):
    query = """
    SELECT p.player_id, p.username
    FROM player p
    JOIN follows f ON p.player_id = f.player_id
    WHERE f.follower_id = %s
    """
    return execute_query(query, params=(player_id,))

if __name__ == '__main__':
    print(find_following(player_id=2420))