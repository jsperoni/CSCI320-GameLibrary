from db_config import execute_query

def get_follows_count(player_id):
    query = "SELECT count(*) FROM follows WHERE follows.player_id = %s"
    followers_count = execute_query(query, params=(player_id,))[0][0]

    query = "SELECT count(*) FROM follows WHERE follows.follower_id = %s"
    following_count = execute_query(query, params=(player_id,))[0][0]

    return followers_count, following_count