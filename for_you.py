from db_config import execute_query

# unfinished
def for_you(player_id):
    query = f"""
    SELECT genre_id, 
    FROM genre g 
        JOIN developer d ON g.game_id = d.game_id
        JOIN publisher p on g.game_id = p.game_id
        JOIN plays
    WHERE f.follower_id = %s
    """
    return execute_query(query, params=(player_id,))

if __name__ == '__main__':
    print(find_following(player_id=2420))