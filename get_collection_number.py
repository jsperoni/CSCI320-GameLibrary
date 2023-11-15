from db_config import execute_query

def get_collection_number(player_id):
    query = "SELECT count(*) FROM collection WHERE collection.player_id = %s"
    return execute_query(query, params=(player_id,))